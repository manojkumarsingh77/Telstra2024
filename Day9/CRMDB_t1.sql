CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Email NVARCHAR(100),
    PhoneNumber NVARCHAR(15),
    RegistrationDate DATE
);

CREATE TABLE CustomerContacts (
    ContactID INT PRIMARY KEY,
    CustomerID INT,
    ContactDate DATE,
    ContactType NVARCHAR(50), -- 'Email', 'Phone', 'In-Person'
    ContactDescription NVARCHAR(255),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
