CREATE TABLE `Orders` (
  `order_number` integer PRIMARY KEY,
  `type` varchar(255),
  `state` varchar(255)
);

CREATE TABLE `Services` (
  `order_number` integer,
  `date_created` date,
  `service_state` varchar(255)
);

CREATE TABLE `Comments` (
  `comment_id` integer PRIMARY KEY,
  `order_number` integer,
  `responder_name` varchar(255),
  `comment` text
);

CREATE TABLE `People` (
  `order_number` integer,
  `last_name` varchar(255),
  `first_name` varchar(255),
  `role` varchar(255),
  `phone` varchar(255),
  `email_address` varchar(255)
);

CREATE TABLE `IP_Addresses` (
  `order_number` integer,
  `ip_address` varchar(255)
);

CREATE TABLE `follows` (
  `following_user_id` integer,
  `followed_user_id` integer,
  `created_at` timestamp
);

CREATE TABLE `users` (
  `id` integer PRIMARY KEY,
  `username` varchar(255),
  `role` varchar(255),
  `created_at` timestamp
);

CREATE TABLE `posts` (
  `id` integer PRIMARY KEY,
  `title` varchar(255),
  `body` text COMMENT 'Content of the post',
  `user_id` integer,
  `status` varchar(255),
  `created_at` timestamp
);

ALTER TABLE `Services` ADD FOREIGN KEY (`order_number`) REFERENCES `Orders` (`order_number`);

ALTER TABLE `Comments` ADD FOREIGN KEY (`order_number`) REFERENCES `Orders` (`order_number`);

ALTER TABLE `People` ADD FOREIGN KEY (`order_number`) REFERENCES `Orders` (`order_number`);

ALTER TABLE `IP_Addresses` ADD FOREIGN KEY (`order_number`) REFERENCES `Orders` (`order_number`);

ALTER TABLE `posts` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `follows` ADD FOREIGN KEY (`following_user_id`) REFERENCES `users` (`id`);

ALTER TABLE `follows` ADD FOREIGN KEY (`followed_user_id`) REFERENCES `users` (`id`);
