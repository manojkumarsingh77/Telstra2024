-- Create table for Customer_Churn
CREATE TABLE Customer_Churn (
    CustomerID NVARCHAR(50) PRIMARY KEY,
    Gender NVARCHAR(10),
    SeniorCitizen BIT,
    Partner NVARCHAR(10),
    Dependents NVARCHAR(10),
    Tenure INT,
    PhoneService NVARCHAR(10),
    MultipleLines NVARCHAR(20),
    InternetService NVARCHAR(20),
    OnlineSecurity NVARCHAR(20),
    OnlineBackup NVARCHAR(20),
    DeviceProtection NVARCHAR(20),
    TechSupport NVARCHAR(20),
    StreamingTV NVARCHAR(20),
    StreamingMovies NVARCHAR(20),
    Contract NVARCHAR(20),
    PaperlessBilling NVARCHAR(10),
    PaymentMethod NVARCHAR(50),
    MonthlyCharges DECIMAL(10, 2),
    TotalCharges DECIMAL(10, 2),
    Churn NVARCHAR(10)
);

-- Create table for Network_Performance
CREATE TABLE Network_Performance (
    Region NVARCHAR(50),
    Date DATE,
    DownloadSpeed_Mbps DECIMAL(10, 2),
    UploadSpeed_Mbps DECIMAL(10, 2),
    Latency_ms INT,
    PacketLoss_Percent DECIMAL(5, 2),
    Jitter_ms INT
);
