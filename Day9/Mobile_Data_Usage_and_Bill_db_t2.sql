CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FullName NVARCHAR(100),
    Email NVARCHAR(100)
);

CREATE TABLE Subscriptions (
    SubscriptionID INT PRIMARY KEY,
    CustomerID INT,
    PlanType NVARCHAR(50), -- 'Prepaid', 'Postpaid'
    StartDate DATE,
    EndDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE DataUsage (
    UsageID INT PRIMARY KEY,
    SubscriptionID INT,
    UsageDate DATE,
    DataUsedMB DECIMAL(10,2),
    FOREIGN KEY (SubscriptionID) REFERENCES Subscriptions(SubscriptionID)
);

CREATE TABLE Billing (
    BillID INT PRIMARY KEY,
    SubscriptionID INT,
    BillingDate DATE,
    AmountDue DECIMAL(10,2),
    PaymentStatus NVARCHAR(50) -- 'Paid', 'Unpaid'
);
