# 公司架構參考

- [公司架構參考](#公司架構參考)
  - [公司部門範例與說明](#公司部門範例與說明)
  - [公司結構與部門功能問答](#公司結構與部門功能問答)
  - [從訂單編號取的下單日期並計算與今日的天數差距](#從訂單編號取的下單日期並計算與今日的天數差距)

## 公司部門範例與說明

1. **Marketing and Sales Department (MSD)**: This department is responsible for promoting the company's products or services, generating leads, and converting these leads into customers¹³.
    - Positions:
      - Marketing Manager (MM)
      - Sales Manager (SM)
      - Business Development Executive (BDE)

2. **Finance Department (FD)**: This department manages the company's finances, including budgeting, financial reporting, and financial planning¹³.
    - Positions:
      - Finance Manager (FM)
      - Financial Analyst (FA)
      - Accountant (AC)

3. **Production/Operations Department (POD)**: This department manages the day-to-day activities required to produce and distribute the company's products or services¹.
    - Positions:
      - Operations Manager (OM)
      - Production Manager (PM)
      - Logistics Coordinator (LC)

4. **Research and Development Department (RDD)**: This department is responsible for developing new and existing products or services. They conduct research and development to create innovative offerings that meet customer needs¹³.
    - Positions:
      - Research Scientist (RS)
      - Product Development Manager (PDM)
      - R&D Engineer (RDE)

5. **Customer Service Department (CSD)**: This department handles customer inquiries, complaints, and provides after-sales support³.
    - Positions:
      - Customer Service Representative (CSR)
      - Customer Service Manager (CSM)
      - Support Specialist (SS)

6. **Purchasing Department (PD)**: This department is responsible for procuring goods and services for the organization¹.
    - Positions:
      - Purchasing Manager (PM)
      - Procurement Specialist (PS)
      - Buyer (BY)

7. **IT Department (ITD)**: This department is responsible for managing the company's information technology infrastructure⁴.
    - Positions:
      - IT Manager (ITM)
      - Network Administrator (NA)
      - Software Developer (SD)

---

Sure, here are some positions that you might find in a mining and mineral company:

1. **Blaster (BL)**: A mining blaster handles the care, transportation, and use of explosive material during mining operations¹.
2. **Underground Miner (UM)**: An underground miner performs duties such as drilling, blasting, mu
3. cking, bolting, and installing utilities within the mine¹.
4. **Heavy Equipment Operator (HEO)**: A heavy equipment operator maintains, stores, and operates heavy equipment such as conveyors, bulldozers, excavators, and cranes¹.
5. **Driller (DR)**: A driller is responsible for drilling holes for blasting in the mining operations³.
6. **Electrician (EL)**: An electrician is responsible for the electrical systems in the mine³.
7. **Material Planner (MP)**: A material planner is responsible for planning and coordinating material use in the mining operations³.
8. **Health and Safety Specialist (HSS)**: A health and safety specialist ensures the safety of the workers and compliance with health and safety regulations³.
9. **Mine Manager (MM)**: A mine manager oversees the mining operations and ensures they are carried out efficiently and safely³.
10. **Chemist (CH)**: A chemist may analyze the particles and makeup of minerals or other materials extracted².
11. **Geological Engineer (GE)**: A geological engineer designs mines to ensure minerals' safe and efficient removal².

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
