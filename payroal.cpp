#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

class payroll {
   ifstream fin;
   char employeeid[12];
   char employeename[20];
   char maritalstatus;
   int hoursworked, overtime;
   double hourlyrate, overtimepay, regularpay, grosspay, taxrate, taxamount, netpay;

   void calculategrosspay();
   void calculatetax();
   void calculatenetpay();
   void printheadings();
   void printdata();

public:
   payroll();
   ~payroll();
   void printreport();
};

payroll::payroll() {
   fin.open("payroll.dat");
}

payroll::~payroll() {
   fin.close();
}

void payroll::calculategrosspay() {
   if (hoursworked > 40) {
      overtime = hoursworked - 40;
      regularpay = hoursworked * hourlyrate;
      overtimepay = overtime * (hourlyrate * 1.5);
      grosspay = regularpay + overtimepay;
   }
   else {
      grosspay = hoursworked * hourlyrate;
   }
}

void payroll::calculatetax() {
#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
using namespace std;

class Employee {
protected:
   char employeeid[12];
   char employeename[20];
   char maritalstatus;
   double grosspay, taxamount, netpay;

public:
   virtual void calculategrosspay() = 0;
   virtual void calculatetax() = 0;
   virtual void calculatenetpay() = 0;
   virtual void printdata() = 0;
   double getNetPay() const { return netpay; }
};

class HourlyEmployee : public Employee {
private:
   int hoursworked, overtime;
   double hourlyrate, overtimepay, regularpay;

public:
   HourlyEmployee(const char* id, const char* name, char status, int hours, double rate)
      : hoursworked(hours), hourlyrate(rate) {
      strcpy(employeeid, id);
      strcpy(employeename, name);
      maritalstatus = status;
   }

   void calculategrosspay() override {
      if (hoursworked > 40) {
         overtime = hoursworked - 40;
         regularpay = hoursworked * hourlyrate;
         overtimepay = overtime * (hourlyrate * 1.5);
         grosspay = regularpay + overtimepay;
      }
      else {
         grosspay = hoursworked * hourlyrate;
      }
   }

   void calculatetax() override {
      if (grosspay >= 500)
         taxamount = grosspay * 0.30;
      else if (grosspay > 200.00)
         taxamount = grosspay * 0.20;
      else
         taxamount = grosspay * 0.10;

      if (maritalstatus == 'S' || maritalstatus == 's')
         taxamount += grosspay * 0.05;
   }

   void calculatenetpay() override {
      netpay = grosspay - taxamount;
   }

   void printdata() override {
      cout << setprecision(2) << fixed << showpoint;
      cout << setw(6) << employeename << setw(12) << employeeid << setw(4)
           << hoursworked << setw(3) << overtime << setw(8) << regularpay << setw(8)
           << overtimepay << setw(8) << grosspay << setw(8) << taxamount << setw(8)
           << netpay << endl;
   }
};

class SalaryEmployee : public Employee {
private:
   double yearlysalary, overtimehours, hourlyrate;

public:
   SalaryEmployee(const char* id, const char* name, char status, double salary, double overtime)
      : yearlysalary(salary), overtimehours(overtime) {
      strcpy(employeeid, id);
      strcpy(employeename, name);
      maritalstatus = status;
   }

   void calculategrosspay() override {
      double weeklysalary = yearlysalary / 52;
      hourlyrate = weeklysalary / 40;
      overtimepay = overtimehours * (hourlyrate * 1.5);
      grosspay = weeklysalary + overtimepay;
   }

   void calculatetax() override {
      if (grosspay >= 500)
         taxamount = grosspay * 0.30;
      else if (grosspay > 200.00)
         taxamount = grosspay * 0.20;
      else
         taxamount = grosspay * 0.10;

      if (maritalstatus == 'S' || maritalstatus == 's')
         taxamount += grosspay * 0.05;
   }

   void calculatenetpay() override {
      netpay = grosspay - taxamount;
   }

   void printdata() override {
      cout << setprecision(2) << fixed << showpoint;
      cout << setw(6) << employeename << setw(12) << employeeid << setw(4)
           << overtimehours << setw(3) << "N/A" << setw(8) << "N/A" << setw(8)
           << overtimepay << setw(8) << grosspay << setw(8) << taxamount << setw(8)
           << netpay << endl;
   }
};

class Payroll {
private:
   Employee** employees;
   int numEmployees;

public:
   Payroll() {
      employees = nullptr;
      numEmployees = 0;
   }

   ~Payroll() {
      for (int i = 0; i < numEmployees; i++) {
         delete employees[i];
      }
      delete[] employees;
   }

   void addEmployee(Employee* employee) {
      Employee** temp = new Employee*[numEmployees + 1];
      for (int i = 0; i < numEmployees; i++) {
         temp[i] = employees[i];
      }
      temp[numEmployees] = employee;
      delete[] employees;
      employees = temp;
      numEmployees++;
   }

   void printReport() {
      cout << setw(45) << "-PAYROLL REPORT-" << endl;
      cout << "------------------------------------------------------------------------------" << endl;
      cout << " NAME      ID       HW OT  RT-PAY  OT-PAY  GROSS    TAX   NETPAY" << endl;
      cout << "------------------------------------------------------------------------------" << endl;

      for (int i = 0; i < numEmployees; i++) {
         employees[i]->calculategrosspay();
         employees[i]->calculatetax();
         employees[i]->calculatenetpay();
         employees[i]->printdata();
      }

      cout << "------------------------------------------------------------------------------" << endl;

      // Find minimum and maximum net pay
      double minNetPay = employees[0]->getNetPay();
      double maxNetPay = employees[0]->getNetPay();
      for (int i = 1; i < numEmployees; i++) {
         double netPay = employees[i]->getNetPay();
         if (netPay < minNetPay)
            minNetPay = netPay;
         if (netPay > maxNetPay)
            maxNetPay = netPay;
      }

      cout << "Minimum Net Pay: $" << minNetPay << endl;
      cout << "Maximum Net Pay: $" << maxNetPay << endl;

      // Sort employees based on net pay (ascending order)
      sort(employees, employees + numEmployees, [](const Employee* a, const Employee* b) {
         return a->getNetPay() < b->getNetPay();
      });

      cout << "Employees Sorted by Net Pay (Ascending Order):" << endl;
      for (int i = 0; i < numEmployees; i++) {
         cout << employees[i]->employeename << " - Net Pay: $" << employees[i]->getNetPay() << endl;
      }
   }
};

int main() {
   Payroll payroll;

   // Add hourly-based employees
   payroll.addEmployee(new HourlyEmployee("E001", "John Doe", 'S', 45, 15.0));
   payroll.addEmployee(new HourlyEmployee("E002", "Jane Smith", 'M', 50, 20.0));

   // Add salary-based employees
   payroll.addEmployee(new SalaryEmployee("E003", "Mike Johnson", 'S', 52000.0, 5));
   payroll.addEmployee(new SalaryEmployee("E004", "Emily Davis", 'M', 60000.0, 3));

   // Print payroll report
   payroll.printReport();

   return 0;
}

   payroll employee;
   employee.printreport();
   return 0;
}
