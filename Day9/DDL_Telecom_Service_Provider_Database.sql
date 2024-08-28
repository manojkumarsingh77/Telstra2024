
/*
Here is a comprehensive real-time telecommunications scenario that covers various aspects of SQL operations, with a focus on Azure SQL, DML, DDL, and working with large datasets. 
This scenario will include a step-by-step guide to implementing a database with 10,000 rows and 40 business query requirements.
*/
/*
Scenario: Telecom Service Provider Database
Objective:
To create a database for managing customer information, service subscriptions, usage details, and billing for a telecommunications company. The database will be designed to handle large datasets and support various SQL operations.
*/

-- Customers Table:

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Email NVARCHAR(100),
    PhoneNumber NVARCHAR(15),
    RegistrationDate DATE,
    Status NVARCHAR(20)
);

-- Subscriptions Table:
CREATE TABLE Subscriptions (
    SubscriptionID INT PRIMARY KEY IDENTITY(1,1),
    CustomerID INT,
    PlanType NVARCHAR(50), -- 'Prepaid', 'Postpaid'
    StartDate DATE,
    EndDate DATE,
    Status NVARCHAR(20),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- UsageDetails Table:
CREATE TABLE UsageDetails (
    UsageID INT PRIMARY KEY IDENTITY(1,1),
    SubscriptionID INT,
    UsageDate DATE,
    DataUsedMB DECIMAL(10,2),
    MinutesUsed DECIMAL(10,2),
    MessagesSent INT,
    FOREIGN KEY (SubscriptionID) REFERENCES Subscriptions(SubscriptionID)
);

-- Billing Table:
CREATE TABLE Billing (
    BillID INT PRIMARY KEY IDENTITY(1,1),
    SubscriptionID INT,
    BillingDate DATE,
    AmountDue DECIMAL(10,2),
    PaymentStatus NVARCHAR(50), -- 'Paid', 'Unpaid'
    FOREIGN KEY (SubscriptionID) REFERENCES Subscriptions(SubscriptionID)
);

