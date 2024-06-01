SELECT * FROM World_layoffs.layoffs;

-- MAKING A COPY OF RAW DATA 
CREATE TABLE layoffs_staging like layoffs;
INSERT layoffs_staging SELECT * FROM layoffs;
SELECT * FROM layoffs_staging;

-- Remove Duplicates
WITH duplicate_cte AS (
SELECT *, ROW_NUMBER() OVER (PARTITION BY company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions) AS row_num FROM layoffs_staging)
SELECT * FROM duplicate_cte WHERE row_num > 1;
CREATE TABLE `layoffs_staging2` (
  `company` text,
  `location` text,
  `industry` text,
  `total_laid_off` int DEFAULT NULL,
  `percentage_laid_off` text,
  `date` text,
  `stage` text,
  `country` text,
  `funds_raised_millions` int DEFAULT NULL,
  `row_num` INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
SELECT * FROM layoffs_staging2 ; 
INSERT layoffs_staging2 SELECT *, ROW_NUMBER() OVER (PARTITION BY company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions) AS row_num FROM layoffs_staging;
delete FROM layoffs_staging2 WHERE row_num > 1;

-- Standardize the Data
SELECT company, TRIM(company) FROM layoffs_staging2;
UPDATE layoffs_staging2 SET company = TRIM(company);
UPDATE layoffs_staging2 SET country = TRIM(TRAILING '.' FROM country);
UPDATE layoffs_staging2 SET `date` = str_to_date(`date`, '%m/%d/%Y');
ALTER TABLE layoffs_staging2 MODIFY column `date` DATE;
SELECT * FROM layoffs_staging2 ;

-- Null Values or blank Values
SELECT * FROM layoffs_staging2 WHERE total_laid_off is NULL and percentage_laid_off is NULL;
SELECT * FROM layoffs_staging2 WHERE industry is null OR industry = ' ';
UPDATE layoffs_staging2 set industry = null where industry = ' ';
update layoffs_staging2  t1 join layoffs_staging2 t2 on t1.company = t2.company set t1.industry =t2.industry where t1.industry is null and t2.industry is not null;
SELECT * FROM layoffs_staging2 ;

-- Remove any Columns
 SELECT * FROM layoffs_staging2 where total_laid_off is null and percentage_laid_off is null ;
 delete FROM layoffs_staging2 where total_laid_off is null and percentage_laid_off is null ;
 alter table layoffs_staging2 drop column row_num;
 SELECT * FROM layoffs_staging2;