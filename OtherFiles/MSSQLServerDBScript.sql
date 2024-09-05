-- Create Database
CREATE DATABASE TelcoDatabase;
GO

USE TelcoDatabase;
GO

-- Create Tables
CREATE TABLE Customers (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    PhoneNumber VARCHAR(15),
    Email VARCHAR(100),
    Address VARCHAR(255),
    City VARCHAR(50),
    State VARCHAR(50),
    ZipCode VARCHAR(10),
    SignupDate DATE
);

CREATE TABLE ServicePlans (
    PlanID INT IDENTITY(1,1) PRIMARY KEY,
    PlanName VARCHAR(100),
    PlanType VARCHAR(50),
    MonthlyCost DECIMAL(10,2),
    DataLimit INT,  -- in GB
    VoiceLimit INT,  -- in minutes
    SMSLimit INT,  -- in number of SMS
    OverageCharge DECIMAL(10,2)  -- charge per extra GB/minute/SMS
);

CREATE TABLE CustomerPlans (
    CustomerPlanID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT,
    PlanID INT,
    ActivationDate DATE,
    DeactivationDate DATE NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (PlanID) REFERENCES ServicePlans(PlanID)
);

CREATE TABLE CallDataRecords (
    CDRID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT,
    CallDateTime DATETIME,
    CallDuration INT,  -- in seconds
    CallType VARCHAR(20),  -- e.g., Local, STD, ISD
    DataUsage DECIMAL(10,2),  -- in MB
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE Payments (
    PaymentID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT,
    PaymentDate DATE,
    Amount DECIMAL(10,2),
    PaymentMethod VARCHAR(50),  -- e.g., Credit Card, Debit Card, Net Banking, UPI
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE ServiceIssues (
    IssueID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT,
    IssueDate DATE,
    IssueType VARCHAR(100),  -- e.g., Network Issue, Billing Issue, Service Issue
    ResolutionDate DATE NULL,
    IssueStatus VARCHAR(20),  -- e.g., Open, Closed, In Progress
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Insert Sample Data

-- Insert into Customers
INSERT INTO Customers (FirstName, LastName, PhoneNumber, Email, Address, City, State, ZipCode, SignupDate)
SELECT TOP 1000
    'FirstName' + CAST(ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS VARCHAR),
    'LastName' + CAST(ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS VARCHAR),
    '123456789' + CAST(ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) % 10 AS VARCHAR),
    'email' + CAST(ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS VARCHAR) + '@example.com',
    'Address ' + CAST(ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS VARCHAR),
    'CityName',
    'StateName',
    '12345',
    DATEADD(DAY, -ABS(CHECKSUM(NEWID())) % 3650, GETDATE())
FROM sys.all_columns;

-- Insert into ServicePlans
INSERT INTO ServicePlans (PlanName, PlanType, MonthlyCost, DataLimit, VoiceLimit, SMSLimit, OverageCharge)
VALUES 
('Basic Plan', 'Prepaid', 199.99, 10, 100, 50, 1.99),
('Standard Plan', 'Postpaid', 499.99, 50, 500, 200, 0.99),
('Premium Plan', 'Postpaid', 999.99, 100, 1000, 500, 0.49),
('Unlimited Plan', 'Postpaid', 1499.99, 1000, 5000, 2000, 0);

-- Insert into CustomerPlans
INSERT INTO CustomerPlans (CustomerID, PlanID, ActivationDate, DeactivationDate)
SELECT 
    C.CustomerID,
    P.PlanID,
    DATEADD(DAY, -ABS(CHECKSUM(NEWID())) % 3650, GETDATE()),
    NULL
FROM 
    (SELECT TOP 1000 CustomerID FROM Customers) C,
    (SELECT TOP 4 PlanID FROM ServicePlans) P;

-- Insert into CallDataRecords
INSERT INTO CallDataRecords (CustomerID, CallDateTime, CallDuration, CallType, DataUsage)
SELECT 
    C.CustomerID,
    DATEADD(SECOND, -ABS(CHECKSUM(NEWID())) % 1000000, GETDATE()),
    ABS(CHECKSUM(NEWID())) % 3600,
    CASE ABS(CHECKSUM(NEWID())) % 3 WHEN 0 THEN 'Local' WHEN 1 THEN 'STD' ELSE 'ISD' END,
    ABS(CHECKSUM(NEWID())) % 1024 * 1.0
FROM 
    (SELECT TOP 1000 CustomerID FROM Customers) C;

-- Insert into Payments
INSERT INTO Payments (CustomerID, PaymentDate, Amount, PaymentMethod)
SELECT 
    C.CustomerID,
    DATEADD(DAY, -ABS(CHECKSUM(NEWID())) % 3650, GETDATE()),
    CASE WHEN P.PlanID = 1 THEN 199.99 WHEN P.PlanID = 2 THEN 499.99 ELSE 999.99 END,
    CASE ABS(CHECKSUM(NEWID())) % 3 WHEN 0 THEN 'Credit Card' WHEN 1 THEN 'Debit Card' ELSE 'Net Banking' END
FROM 
    (SELECT TOP 1000 CustomerID FROM Customers) C
JOIN 
    CustomerPlans P ON C.CustomerID = P.CustomerID;

-- Insert into ServiceIssues
INSERT INTO ServiceIssues (CustomerID, IssueDate, IssueType, ResolutionDate, IssueStatus)
SELECT 
    C.CustomerID,
    DATEADD(DAY, -ABS(CHECKSUM(NEWID())) % 3650, GETDATE()),
    CASE ABS(CHECKSUM(NEWID())) % 3 WHEN 0 THEN 'Network Issue' WHEN 1 THEN 'Billing Issue' ELSE 'Service Issue' END,
    CASE WHEN ABS(CHECKSUM(NEWID())) % 2 = 0 THEN DATEADD(DAY, -ABS(CHECKSUM(NEWID())) % 3650, GETDATE()) ELSE NULL END,
    CASE ABS(CHECKSUM(NEWID())) % 3 WHEN 0 THEN 'Open' WHEN 1 THEN 'Closed' ELSE 'In Progress' END
FROM 
    (SELECT TOP 1000 CustomerID FROM Customers) C;
GO

-- Sample Business Queries

-- Query 1: Identify the top 10 customers who have spent the most money in the last year.
SELECT TOP 10 
    C.FirstName, 
    C.LastName, 
    SUM(P.Amount) AS TotalSpent
FROM 
    Payments P
JOIN 
    Customers C ON P.CustomerID = C.CustomerID
WHERE 
    P.PaymentDate >= DATEADD(YEAR, -1, GETDATE())
GROUP BY 
    C.FirstName, C.LastName
ORDER BY 
    TotalSpent DESC;

-- Query 2: Determine which service plan has the most active subscriptions.
SELECT 
    SP.PlanName, 
    COUNT(CP.CustomerPlanID) AS ActiveSubscriptions
FROM 
    CustomerPlans CP
JOIN 
    ServicePlans SP ON CP.PlanID = SP.PlanID
WHERE 
    CP.DeactivationDate IS NULL
GROUP BY 
    SP.PlanName
ORDER BY 
    ActiveSubscriptions DESC;

-- Query 3: List customers who have exceeded their data limit in the current month.
SELECT 
    C.FirstName, 
    C.LastName, 
    SUM(CDR.DataUsage) AS TotalDataUsage, 
    SP.DataLimit
FROM 
    CallDataRecords CDR
JOIN 
    CustomerPlans CP ON CDR.CustomerID = CP.CustomerID
JOIN 
    ServicePlans SP ON CP.PlanID = SP.PlanID
JOIN 
    Customers C ON CDR.CustomerID = C.CustomerID
WHERE 
    MONTH(CDR.CallDateTime) = MONTH(GETDATE())
    AND YEAR(CDR.CallDateTime) = YEAR(GETDATE())
    AND CP.DeactivationDate IS NULL
GROUP BY 
    C.FirstName, 
    C.LastName, 
    SP.DataLimit
HAVING 
    SUM(CDR.DataUsage) > SP.DataLimit;

Query 4: Provide a list of all unresolved service issues, categorized by issue type.
SELECT 
    SI.IssueType, 
    COUNT(SI.IssueID) AS UnresolvedIssues
FROM 
    ServiceIssues SI
WHERE 
    SI.IssueStatus != 'Closed'
GROUP BY 
    SI.IssueType;

Query 5: Identify customers who have not used any services (calls or data) in the last 3 months but have an active subscription.

We’ll break it down into a more straightforward approach:

    1.  Identify all customers with an active subscription.
    2.  Identify customers with service usage in the last 3 months.
    3.  Exclude those who have service usage from the list of all active customers.

SELECT 
    C.CustomerID, 
    C.FirstName, 
    C.LastName, 
    CP.ActivationDate
FROM 
    Customers C
JOIN 
    CustomerPlans CP ON C.CustomerID = CP.CustomerID
WHERE 
    CP.DeactivationDate IS NULL
    AND C.CustomerID NOT IN (
        SELECT DISTINCT CDR.CustomerID 
        FROM CallDataRecords CDR
        WHERE CDR.CallDateTime >= DATEADD(MONTH, -3, GETDATE())
    );
-- Insert a few customers without recent activity
INSERT INTO Customers (FirstName, LastName, PhoneNumber, Email, Address, City, State, ZipCode, SignupDate)
VALUES ('John', 'Doe', '1234567890', 'john.doe@example.com', '123 Main St', 'CityName', 'StateName', '12345', '2021-01-01');

-- Assign these customers a service plan
INSERT INTO CustomerPlans (CustomerID, PlanID, ActivationDate, DeactivationDate)
VALUES ((SELECT MAX(CustomerID) FROM Customers), 1, '2021-01-01', NULL);

-- Run the query again to check if these customers are picked up as inactive
