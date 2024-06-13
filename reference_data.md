# 公司架構參考

- [公司架構參考](#公司架構參考)
  - [公司部門範例與說明](#公司部門範例與說明)
  - [公司結構與部門功能問答](#公司結構與部門功能問答)
  - [從訂單編號取的下單日期並計算與今日的天數差距](#從訂單編號取的下單日期並計算與今日的天數差距)
  - [polymorphic associations](#polymorphic-associations)
  - [從訂單找交易對象](#從訂單找交易對象)

## 公司部門範例與說明

1. **Marketing and Sales Department (MSD)**: This department is responsible for promoting the company's products or services, generating leads, and converting these leads into customers¹³.
    - Positions:
      1. Marketing Director (行銷總監) - MD
      2. Marketing Manager (行銷經理) - MMG
      3. Marketing Coordinator (行銷協調員) - MCO
      4. Marketing Analyst (行銷分析師) - MAN
      5. Marketing Specialist (行銷專員) - MS
      6. Sales Director (銷售總監) - SD
      7. Sales Manager (銷售經理) - SMG
      8. Sales Representative (銷售代表) - SRE
      9. Sales Specialist (銷售專員) - SS
      10. Sales Consultant (銷售顧問) - SC

2. **Finance Department (FD)**: This department manages the company's finances, including budgeting, financial reporting, and financial planning¹³.
    - Positions:
      1. Finance Manager (財務經理) - FMG
      2. Financial Analyst (財務分析師) - FAN
      3. Financial Controller (財務控制員) - FCO
      4. Finance Clerk (財務文員) - FCL
      5. Financial Advisor (財務顧問) - FAD
      6. Finance Manager (財務經理) - FM
      7. Accountant (會計師) - ACC
      8. Financial Analyst (財務分析師) - FA
      9. Auditor (審計員) - AUD
      10. Controller (控制員) - CON
      11. Treasurer (財務主管) - TRE
      12. Budget Analyst (預算分析師) - BA
      13. Tax Specialist (稅務專員) - TS
      14. Payroll Clerk (工資管理員) - PC

3. **Production/Operations Department (POD)**: This department manages the day-to-day activities required to produce and distribute the company's products or services¹.
    - Positions:
      1. Operations Manager (運營經理) - OMG
      2. Production Manager (生產經理) - PMG
      3. Operations Analyst (運營分析師) - OAN
      4. Production Planner (生產規劃員) - PPL
      5. Operations Manager (運營經理) - OM
      6. Production Supervisor (生產主管) - PS
      7. Warehouse Specialist (倉管人員) - WHS
      8. Inventory Manager (庫存經理) - IM
      9. Plant Manager (工廠經理) - PM
      10. Production Worker (生產工人) - PW
      11. Quality Control Specialist (品質控制專員) - QCS
      12. Production Planner (生產計劃員) - PP
      13. Logistics Coordinator (物流協調員) - LC
      14. Operations Analyst (運營分析師) - OA
      15. Quality Assurance Manager (品質保證經理) - QAM

4. **Research and Development Department (RDD)**: This department is responsible for developing new and existing products or services. They conduct research and development to create innovative offerings that meet customer needs¹³.
    - Positions:
      1. Research Scientist (研究科學家) - RSC
      2. Development Engineer (開發工程師) - DEN
      3. Research Analyst (研究分析師) - RAN
      4. Development Manager (開發經理) - DMG
      5. Research Coordinator (研究協調員) - RCO
      6. Research Scientist (研究科學家) - RS
      7. Development Engineer (開發工程師) - DE
      8. Lab Technician (實驗室技術員) - LT
      9. Product Manager (產品經理) - PM
      10. Research Associate (研究助理) - RA
      11. Data Analyst (數據分析師) - DA
      12. Project Manager (項目經理) - PJM
      13. Test Engineer (測試工程師) - TE
      14. Research Director (研究總監) - RD
      15. Development Manager (開發經理) - DM

5. **Customer Service Department (CSD)**: This department handles customer inquiries, complaints, and provides after-sales support³.
    - Positions:
      1. Customer Service Manager (客戶服務經理) - CSM
      2. Customer Service Representative (客戶服務代表) - CSR
      3. Customer Support Specialist (客戶支援專員) - CSS
      4. Customer Experience Manager (客戶體驗經理) - CEM
      5. Customer Service Representative (客服代表) - CSR
      6. Help Desk Specialist (幫助台專員) - HDS
      7. Customer Service Manager (客服經理) - CSM
      8. Call Center Agent (服務中心代理) - CCA
      9. Technical Support Specialist (技術支援專員) - TSS
      10. Account Manager (客戶經理) - AM
      11. Client Relations Manager (客戶關係經理) - CRM
      12. Service Desk Analyst (服務台分析師) - SDA
      13. Customer Support Engineer (客戶支援工程師) - CSE
      14. Customer Experience Manager (客戶體驗經理) - CEM

6. **Purchasing Department (PD)**: This department is responsible for procuring goods and services for the organization¹.
    - Positions:
      1. Purchasing Manager (採購經理) - PMG
      2. Purchasing Agent (採購代理人) - PAG
      3. Procurement Specialist (採購專員) - PCS
      4. Purchasing Clerk (採購文員) - PCL
      5. Procurement Analyst (採購分析師) - PAN
      6. Purchasing Manager (採購經理) - PM
      7. Buyer (採購員) - BUY
      8. Procurement Specialist (採購專員) - PS
      9. Purchasing Clerk (採購文員) - PC
      10. Supply Chain Analyst (供應鏈分析師) - SCA
      11. Vendor Manager (供應商經理) - VM
      12. Procurement Manager (採購經理) - PRM
      13. Purchasing Coordinator (採購協調員) - PCO
      14. Inventory Control Specialist (庫存控制專員) - ICS
      15. Purchasing Agent (採購代理) - PA

7. **IT Department (ITD)**: This department is responsible for managing the company's information technology infrastructure⁴.
    - Positions:
      1. IT Manager (IT經理) - ITM
      2. IT Technician (IT技術員) - ITT
      3. Network Engineer (網絡工程師) - NEN
      4. Software Developer (軟件開發人員) - SDE
      5. IT Support Specialist (IT支援專員) - ISS
      6. IT Manager (IT經理) - ITM
      7. Systems Administrator (系統管理員) - SA
      8. Network Engineer (網絡工程師) - NE
      9. Database Administrator (數據庫管理員) - DBA
      10. IT Support Specialist (IT支援專員) - ISS
      11. Software Developer (軟件開發員) - SD
      12. IT Analyst (IT分析師) - ITA
      13. IT Project Manager (IT項目經理) - IPM
      14. Security Analyst (安全分析師) - SEC
      15. Web Developer (網頁開發員) - WD

8. **Human Resource Department (HR)**: 人力資源部門
    - Positions:
      1. Human Resources Specialist (人力資源專員) - HRS
      2. Human Resources Manager (人力資源經理) - HRM
      3. Recruitment Specialist (招聘專員) - RS
      4. Training Coordinator (培訓協調員) - TC
      5. Benefits Administrator (福利管理員) - BA
      6. HR Analyst (人力資源分析師) - HRA
      7. Employee Relations Manager (員工關係經理) - ERM
      8. HR Consultant (人力資源顧問) - HRC
      9. Payroll Specialist (薪資專員) - PS
      10. HR Assistant (人力資源助理) - HRA

9. **Mine Department (MD)**
    - Positions:
      1. Mine Blaster Worker (礦山爆破工) - MBW
      2. Underground Miner (地下礦工) - UM
      3. Heavy Equipment Operator (重型設備操作員) - HEO
      4. Driller (鑽孔員) - DR
      5. Electrician (電工) - EL
      6. Material Planner (材料規劃師) - MTP
      7. Health and Safety Specialist (健康與安全專員) - HSS
      8. Mine Manager (礦山經理) - MNM
      9. Chemist (化學家) - CH
      10. Geological Engineer (地質工程師) - GE

---

## 公司結構與部門功能問答

Q:

  In a company finacial department, if an order and invoice is not valid, could FD employee direct edit the data, or they should acknowledge the sales department?

A:

> In a company's financial department, if an order and invoice are found to be invalid, the financial department (FD) employee should typically follow the company's established protocols for such situations. Generally, direct editing of the data by the FD employee is not advisable due to the following reasons:
>
> - **Audit Trail**: Any changes made to financial documents should be traceable. Direct edits can obscure the history of transactions and may cause issues during audits.
>
> - **Separation of Duties**: This is a key principle in internal controls to prevent fraud and errors. The sales department is usually responsible for issuing and validating orders and invoices.
>
> - **Accuracy**: The sales department may have information that the financial department does not, which could affect the validity of the order or invoice.
>
> Therefore, the FD employee should **acknowledge the sales department** and follow these steps:
>
> 1. **Notify**: Inform the sales department of the discrepancy.
> 2. **Collaborate**: Work together with the sales department to understand the issue.
> 3. **Correct**: Once the sales department has reviewed and corrected the information, the FD can update the financial records accordingly.
>
> This process ensures that all changes are made transparently and with the proper checks and balances. It's important to consult the company's policy manual or speak with a supervisor to ensure that the correct procedures are followed. **Communication** and **collaboration** between departments are key to maintaining the integrity of financial records.

## 從訂單編號取的下單日期並計算與今日的天數差距

Q:

my order_id is date based, can I extract the date can get duration between that date and today?
order_id
20240611-zF8

A:

You can achieve this in SQL as well. Here's an example using MySQL:

```sql
SELECT 
    order_id, 
    DATEDIFF(CURDATE(), STR_TO_DATE(SUBSTRING_INDEX(order_id, '-', 1), '%Y%m%d')) AS duration
FROM 
    orders_table
WHERE 
    order_id = '20240611-zF8';
```

In this query, `SUBSTRING_INDEX(order_id, '-', 1)` is used to extract the date part from the `order_id`. `STR_TO_DATE` is then used to convert this string to a date. `DATEDIFF` is used to calculate the difference in days between the current date (`CURDATE()`) and the order date. The result is selected as `duration`.

Please replace `'20240611-zF8'` with your actual `order_id` and `orders_table` with your actual table name when you run the query.

This query assumes that the date in the `order_id` is in the format `YYYYMMDD`. If the format is different, you would need to adjust the format string in the `STR_TO_DATE` function accordingly.

Also, please note that SQL syntax can vary between different database systems. If you're not using MySQL, you might need to adjust the query to match your database system's syntax. For example, in PostgreSQL, you would use `CURRENT_DATE` instead of `CURDATE()`, and the date format string would be `'YYYYMMDD'` instead of `'%Y%m%d'`. If you're using a different database system and need help adjusting the query, please let me know.

## polymorphic associations

Q:

In a database, can an attribute of a table reference 2 table?
Here I have 2 entities, Client and Supplier, I want TransactionParty in Oders reference these 2 table.

A:

In a relational database, an attribute typically references a single table through a foreign key constraint. However, if you want the `TransactionParty` attribute in the `Orders` table to reference both `Customer` and `Supplier` tables, you cannot directly create two foreign key constraints on the same attribute referencing two different tables.

To achieve this, you can use a design pattern known as **polymorphic associations**. Here's one way to implement it:

1. Modify the `Orders` table to include two separate attributes for the foreign keys, one for customers and one for suppliers:

    ```sql
    Orders (
        OrderNumber: string,
        PaymentDate: date,
        PaymentMethod: string,
        CustomerID: string,
        SupplierID: string
    )
    Primary Key: OrderNumber
    Foreign Key: CustomerID References Customer
    Foreign Key: SupplierID References Supplier
    ```

2. Allow `CustomerID` and `SupplierID` to be nullable, meaning an order can be associated with either a customer or a supplier, but not both at the same time.

3. Add a check constraint to ensure that one and only one of `CustomerID` or `SupplierID` is non-null for each order.

Here's how the modified SQL script might look:

```sql
CREATE TABLE Orders (
    OrderNumber string NOT NULL,
    PaymentDate date NOT NULL,
    PaymentMethod string NOT NULL,
    CustomerID string NULL,
    SupplierID string NULL,
    CONSTRAINT PK_Orders PRIMARY KEY (OrderNumber),
    CONSTRAINT FK_Orders_Customer FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    CONSTRAINT FK_Orders_Supplier FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID),
    CONSTRAINT CHK_Orders_OneParty CHECK (
        (CustomerID IS NOT NULL AND SupplierID IS NULL) OR
        (CustomerID IS NULL AND SupplierID IS NOT NULL)
    )
);
```

This approach ensures that each order is linked to either a customer or a supplier, maintaining the integrity of your database design. Remember to adjust the data types and constraints as per your database's specific requirements. 😊

## 從訂單找交易對象

To record either a customer or supplier in the `交易對象` field of the `收付款明細` table, you can modify the `訂單` (Orders) table to include both a `CustomerID` and a `SupplierID`. Then, in the `收付款明細` (PaymentDetail) table, you can reference the `訂單` table and use a conditional check to determine whether the transaction party is a customer or supplier based on which field is populated. Here's how you can adjust your tables:

With these changes, when you create a record in the `收付款明細` table, you will reference the `OrderNumber`. The `訂單` table will indicate whether the transaction is related to a customer or supplier by checking which ID field (`CustomerID` or `SupplierID`) is filled.

Here's an example of how you might check this in a query:

```sql
SELECT
    pd.BillNumber,
    pd.OrderNumber,
    CASE
        WHEN o.CustomerID IS NOT NULL THEN 'Customer'
        WHEN o.SupplierID IS NOT NULL THEN 'Supplier'
    END AS TransactionPartyType,
    COALESCE(o.CustomerID, o.SupplierID) AS TransactionPartyID,
    pd.BankCode,
    pd.TransactionDate,
    pd.Amount
FROM
    PaymentDetail pd
JOIN
    Orders o ON pd.OrderNumber = o.OrderNumber
```

This SQL query uses a `CASE` statement to determine the type of the transaction party and the `COALESCE` function to get the non-null `CustomerID` or `SupplierID`. This way, you can record and identify whether the transaction party is a customer or supplier without altering the structure of the `收付款明細` table. Remember to adjust your application logic accordingly to handle these changes.
