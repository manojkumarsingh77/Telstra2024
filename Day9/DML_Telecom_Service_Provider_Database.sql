-- 3.1 Insert Sample Data into Customers Table

-- Assuming we are generating data for 10,000 customers
DECLARE @i INT = 1;

WHILE @i <= 10000
BEGIN
    INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber, RegistrationDate, Status)
    VALUES (
        CONCAT('FirstName', @i),
        CONCAT('LastName', @i),
        CONCAT('user', @i, '@telecom.com'),
        CONCAT('123456789', @i % 10),
        DATEADD(DAY, -@i, GETDATE()),
        CASE WHEN @i % 2 = 0 THEN 'Active' ELSE 'Inactive' END
    );
    SET @i = @i + 1;
END;

-- 3.2 Insert Data into Subscriptions Table
DECLARE @i INT = 1;

WHILE @i <= 10000
BEGIN
    INSERT INTO Subscriptions (CustomerID, PlanType, StartDate, EndDate, Status)
    VALUES (
        @i,
        CASE WHEN @i % 2 = 0 THEN 'Postpaid' ELSE 'Prepaid' END,
        DATEADD(MONTH, -(@i % 12), GETDATE()),
        DATEADD(MONTH, @i % 12, GETDATE()),
        CASE WHEN @i % 2 = 0 THEN 'Active' ELSE 'Inactive' END
    );
    SET @i = @i + 1;
END;

-- 3.3 Insert Data into UsageDetails Table
DECLARE @i INT = 1;

WHILE @i <= 10000
BEGIN
    INSERT INTO UsageDetails (SubscriptionID, UsageDate, DataUsedMB, MinutesUsed, MessagesSent)
    VALUES (
        @i,
        DATEADD(DAY, -(@i % 30), GETDATE()),
        RAND() * 5000,
        RAND() * 1000,
        ABS(CHECKSUM(NEWID())) % 500
    );
    SET @i = @i + 1;
END;

-- 3.4 Insert Data into Billing Table
DECLARE @i INT = 1;

WHILE @i <= 10000
BEGIN
    INSERT INTO Billing (SubscriptionID, BillingDate, AmountDue, PaymentStatus)
    VALUES (
        @i,
        DATEADD(MONTH, -(@i % 12), GETDATE()),
        RAND() * 100,
        CASE WHEN @i % 2 = 0 THEN 'Paid' ELSE 'Unpaid' END
    );
    SET @i = @i + 1;
END;


