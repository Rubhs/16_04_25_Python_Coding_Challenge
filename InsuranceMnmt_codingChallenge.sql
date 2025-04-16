CREATE DATABASE InsuranceMnmt;

USE InsuranceMnmt;

CREATE TABLE [User] (
    userId INT PRIMARY KEY IDENTITY(1,1),
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL
);

CREATE TABLE Policy (
    policyId INT PRIMARY KEY IDENTITY(1,1),
    policyName VARCHAR(100),
    premiumAmount DECIMAL(10, 2)
);

CREATE TABLE Client (
    clientId INT PRIMARY KEY IDENTITY(1,1),
    clientName VARCHAR(100),
    contactInfo VARCHAR(255),
    policyId INT,
    FOREIGN KEY (policyId) REFERENCES Policy(policyId)
);

CREATE TABLE Claim (
    claimId INT PRIMARY KEY IDENTITY(1,1),
    claimNumber VARCHAR(50),
    dateFiled DATE,
    claimAmount DECIMAL(10, 2),
    status VARCHAR(50),
    policyId INT,
    clientId INT,
    FOREIGN KEY (policyId) REFERENCES Policy(policyId),
    FOREIGN KEY (clientId) REFERENCES Client(clientId)
);

CREATE TABLE Payment (
    paymentId INT PRIMARY KEY IDENTITY(1,1),
    paymentDate DATE,
    paymentAmount DECIMAL(10, 2),
    clientId INT,
    FOREIGN KEY (clientId) REFERENCES Client(clientId)
);

SELECT * FROM [User];
SELECT * FROM Client;

SELECT * FROM Claim;
SELECT * FROM Payment;


SELECT * FROM Policy;

