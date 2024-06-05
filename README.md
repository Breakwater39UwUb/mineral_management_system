# 礦業會計系統

資料庫系統期末專題

題目:礦業會計系統

指導教授:江季翰

組別:12

組員:

1. 41043118 呂昱諦
2. 41043116 吳枰樟
3. 41043136 俞漢威
4. 41043152 許書和

- [礦業會計系統](#礦業會計系統)
  - [應用情境](#應用情境)
  - [系統需求說明](#系統需求說明)
  - [使用案例](#使用案例)
    - [使用案例圖](#使用案例圖)
  - [完整性限制](#完整性限制)
  - [ER-Diagram](#er-diagram)
  - [實體屬性與關聯說明](#實體屬性與關聯說明)
  - [詳細說明](#詳細說明)
  - [Schema](#schema)
  - [SQL](#sql)
    - [資料表結果圖](#資料表結果圖)
  - [分工](#分工)

## 應用情境

作為礦業開發公司所使用的會計系統,本系統資料庫涵蓋材料、存貨、訂單、物品之儲存,可延伸之應用為訂單、存貨、貿易、會計、管理系統等。

礦業進行開發時,採集到之天然礦物將作為存貨儲存至存貨資料庫。而礦業開發所運用到之各項器具、物品等,將儲存至材料資料庫中。會計系統將以存貨、銷售、與進貨產生的付款收款明細來結算交易。

## 系統需求說明

本系統將存貨、材料或裝置等以物品ID、名稱、存放地、類別、數量、單價、供應商、用途與購置日期等,儲存至物品資料表。其中,存貨無需紀錄供應商、購置日期。員工資料表將儲存員工ID、員工姓名、所屬部門與其職位。

採購部門進貨時,交易訂單應紀錄交易類別、負責員工ID、物品ID、交易對象、訂單編號、付款方式與付款日期,且以交易類別來區分銷售部門訂單區分。銷售部門賣出存貨時,應紀錄之項目如採購部門相同,並透過交易類別區分採購訂單。

生產部門儲存商品時,應紀錄負責員工ID、物品ID、銷貨成本與製造日期,此處物品單價意指商品售價。

會計系統將收付款明細結算交易時,應紀錄專責員工ID與帳單編號。收付款明細將紀錄帳單編號、訂單編號、交易日期、銀行代碼、銀行帳號、銀行名稱、交易對象與金額。

## 使用案例

### 使用案例圖

![Use case diagram](./document/Usecase.png)

## 完整性限制

員工

1. 員工ID:長度為10的字串,不可為空,格式為 `DEP-POS-ID`
   1. 三個部分以 `-` 符號分隔,字母皆為大寫。
   2. DEP代表部門,以2位英文字母編碼。
   3. POS代表職位,以3位英文字母編碼。
   4. ID為3位英文字母與數字編碼。
2. 職位:長度為10的中文字串,須符合公司內的職位名稱,不可為空。
3. 部門:長度為10的中文字串,須符合公司內的部門名稱,不可為空。
4. 姓名:長度為10的中文字串,須符合姓氏+名字順序,不可為空。

物品

1. 物品ID:長度為15的字串,前五碼為大寫英文AAAAA~ZZZZZ,後十碼為正整數0000000000~9999999999。
2. 物品類別:長度為10的中文字串,如礦石類、工具類、材料類,預設值為未分類。
3. 物品名稱:長度為50的中文字串,不可為空。
4. 物品數量:正整數,不可為空,預設值為0。
5. 物品單價:正整數,不可為空,預設值為0。
6. 用途:長度為50的中文字串,可為空,預設值為NULL。
7. 存放地點:長度為50的中文字串,為物品存放的地址。
8. 購置日期:只儲存年月日,不得小於從公司建立日期,預設值為NULL。
9. 供應商:長度為20的中文字串,不可為空。

收付款明細

 1. 帳單編號:長度為10的字母與數字,不可為空。格式如下。
 2. 前3碼為隨機的英文字母及數字
 3. 第4碼為字元"-"
 4. 後6碼為隨機的數字
 5. 訂單編號:長度為12的字串,不可為空,格式如前述。
 6. 交易對象:長度為50的中文字串,不可為空
 7. 銀行代碼:長度為3的字串,不可為空
 8. 銀行名稱:長度為50字串
 9. 銀行帳號:長度為14的字串,7+7(局號+帳號),不可為空
 10. 交易日期:儲存日期時間,不得小於從公司建立日期
 11. 金額:正整數,不可為空

交易關係

1. 訂單編號:長度為12的字串,不可為空,格式如下。
2. 前8碼為下單日期,YYYYMMDD
3. 第9碼為字元"-"
4. 後3碼為隨機的英文字母及數字
5. 物品ID:長度為15的字串。
6. 員工ID:長度為10的字串,不可為空,格式為DEP-POS-ID。
7. 交易類別:長度為2的字串,僅為"購入" 或"銷售",不可為空。
8. 付款日期:儲存日期時間,可為空,不得小於從公司建立日期,預設值為NULL。
9. 付款方式:長度為10的中文字串,可為空,預設值為NULL。
10. 交易對象:長度為50的中文字串,不可為空。

製造關係

1. 員工ID:長度為10的字串,不可為空,格式為DEP-POS-ID。
2. 物品ID:長度為15的字串,格式如前述。
3. 製造日期:儲存日期時間,可為空,不得小於從公司建立日期,預設值為當日。
4. 銷貨成本:正整數,包含零,預設值為NULL。

紀錄關係

1. 員工ID:長度為10的字串,不可為空,格式為DEP-POS-ID。
2. 帳單編號:長度為10的字母與數字,格式如前述。

## ER-Diagram

共有三個實體

1. 物品
2. 員工
3. 收付款明細

共有三個關聯

1. 交易
2. 製造
3. 紀錄

![ER-Diagram](./image)

## 實體屬性與關聯說明

實體

| 實體 | 屬性     | Key | 說明                                             |
| ---- | -------- | --- | ------------------------------------------------ |
| 物品 | 物品ID   |     | 物品的編號，由程式產生。                         |
|      | 物品類別 |     | 物品的名稱。                                     |
|      | 物品名稱 |     | 物品類別，由類別判斷是否為商品。                 |
|      | 物品數量 |     | 物品數量。                                       |
|      | 物品單價 |     | 物品為商品時，指物品售價；否則為購入的物品單價。 |
|      | 用途     |     | 物品存放地點。                                   |
|      | 存放地點 |     | 物品之購入日期。                                 |
|      | 購置日期 |     | 物品之說明欄位。                                 |
|      | 供應商   |     | 購入物品之供應商。                               |

| 實體       | 屬性     | Key         | 說明                                                                               |
| ---------- | -------- | ----------- | ---------------------------------------------------------------------------------- |
| 收付款明細 | 帳單編號 | Primary Key | 紀錄收付款明細的，此編號由系統產生。                                               |
|            | 訂單編號 | Foreign Key | 銷售或進貨訂單上的訂單編號，此編號由系統產生。                                     |
|            | 銀行名稱 |             | 對應銀行代碼之銀行名稱。                                                           |
|            | 交易對象 | Foreign Key | 交易對象可為客戶時，指此為銷售。為本公司時，則為進貨。此欄位參考修交易的交易對象。 |
|            | 銀行代碼 |             | 該銀行對應的三碼數字，由程式檢查其正確性。                                         |
|            | 銀行帳號 |             | 銀行的帳號。                                                                       |
|            | 交易日期 |             | 只儲存年月日。                                                                     |
|            | 金額     |             | 該訂單的金額。                                                                     |

| 實體 | 屬性   | Key         | 說明                             |
| ---- | ------ | ----------- | -------------------------------- |
| 員工 | 員工ID | Primary Key | 員工的ID，由程式產生。           |
|      | 姓名   |             | 員工的姓名。                     |
|      | 部門   |             | 員工部門，該部門需存在於公司中。 |
|      | 職位   |             | 員工職位。                       |

關聯

| 關聯 | 關聯實體 | 關聯實體 | Cardinality | 說明                                                               |
| ---- | -------- | -------- | ----------- | ------------------------------------------------------------------ |
| 交易 | 物品     | 員工     | 多對多      | 至少一位員工會購買工廠的器具與銷售商品，且商品一定會被購入與賣出。 |

| 關聯 | 屬性     | Key | 說明 |
| ---- | -------- | --- | ---- |
| 交易 | 訂單編號 |     |      |
|      | 物品ID   |     |      |
|      | 員工ID   |     |      |
|      | 交易類別 |     |      |
|      | 交易對象 |     |      |
|      | 付款方式 |     |      |
|      | 付款日期 |     |      |

| 關聯 | 關聯實體 | 關聯實體 | Cardinality | 說明                                                       |
| ---- | -------- | -------- | ----------- | ---------------------------------------------------------- |
| 製造 | 物品     | 員工     | 一對多      | 至少一個員工會負責製造商品，且一個商品只會由一位員工負責。 |

| 關聯 | 屬性     | Key | 說明 |
| ---- | -------- | --- | ---- |
| 製造 | 員工ID   |     |      |
|      | 物品ID   |     |      |
|      | 銷貨成本 |     |      |
|      | 製造日期 |     |      |

| 關聯 | 關聯實體 | 關聯實體   | Cardinality | 說明                                                               |
| ---- | -------- | ---------- | ----------- | ------------------------------------------------------------------ |
| 紀錄 | 員工     | 收付款明細 | 一對多      | 至少有一個員工會負責紀錄收付款明細，且一個明細只會由一位員工負責。 |

| 關聯 | 屬性     | Key | 說明 |
| ---- | -------- | --- | ---- |
| 紀錄 | 員工ID   |     |      |
|      | 帳單編號 |     |      |

## 詳細說明

## Schema

## SQL

```SQL
CREATE TABLE Items (
  ItemId char(15) NOT NULL,
  ItemNum int NOT NULL DEFAULT 0,
  ItemValue int NOT NULL DEFAULT 0,
  ItemName varchar(50) NOT NULL,
  ItemClass varchar(10) DEFAULT '未分類',
  ItemPlace varchar(50) DEFAULT NULL,
  ItemUsage varchar(50) DEFAULT NULL,
  ManufacturingDate Date DEFAULT NULL,
  PurchaseDate Date DEFAULT NULL,
  PRIMARY KEY (ItemId) CONSTRAINT chk_Items CHECK (
    ItemNum >= 0
    AND ItemValue >= 0
    AND CostOfGoods >= 0
    AND LENGTH(ItemId) != 0
    AND LENGTH(ItemNum) != 0
    AND LENGTH(ItemValue) != 0
    AND LENGTH(ItemName) != 0
  )
);
```

```SQL
CREATE TABLE Employee (
  EmpId char(15) NOT NULL,
  EmpDepartment varchar(10) NOT NULL,
  EmpPosition varchar(10) NOT NULL,
  EmpName varchar(10) NOT NULL,
  PRIMARY KEY (EmpId) CONSTRAINT chk_Items CHECK (
    LENGTH(EmpId) != 0
    AND LENGTH(EmpDepartment) != 0
    AND LENGTH(EmpPosition) != 0
    AND LENGTH(EmpName) != 0
  )
);
```

```SQL
CREATE TABLE Trade (
  OrderId char(13) NOT NULL,
  TraPartners varchar(50) NOT NULL,
  PayMethod varchar(10) DEFAULT NULL,
  TraClass char(2) NOT NULL,
  TraDate Date NOT NULL,
  EmpId char(15) NOT NULL,
  ItemId char(15) NOT NULL,
  PRIMARY KEY (OrderId),
  FOREIGN KEY (EmpId) REFERENCES Employee(EmpId),
  FOREIGN KEY (ItemId) REFERENCES Items(ItemId)
  CONSTRAINT chk_Trade CHECK (
    LENGTH(OrderId) == 13
    AND LENGTH(TraPartners) != 0
    AND LENGTH(TraClass) != 0
    AND LENGTH(TraDate) != 0
  )
);
```

```SQL
CREATE TABLE Bill (
  BillID varchar(15) NOT NULL,
  OrderId char(13) NOT NULL,
  TraPartners varchar(50) NOT NULL,
  BankID char(3) NOT NULL,
  BankName varchar(50) NOT NULL,
  BankAcc char(14) NOT NULL,
  PayDate Date NOT NULL,
  TraNum int NOT NULL DEFAULT 0, -- total amount
  PRIMARY KEY (BillID),
  FOREIGN KEY (TraPartners) REFERENCES Trade(TraPartners),
  FOREIGN KEY (OrderId) REFERENCES Trade(OrderId),
  CONSTRAINT chk_Bill CHECK (
    LENGTH(BankID) == 3
    AND LENGTH(BankAcc) == 14
    AND LENGTH(BillID) != 0
    AND LENGTH(BankName) != 0
    AND LENGTH(PayDate) != 0
    AND LENGTH(TraNum) != 0
  )
);
```

```SQL
CREATE TABLE Record (
  EmpId char(15) NOT NULL,
  BillID varchar(15) NOT NULL,
  FOREIGN KEY (EmpId) REFERENCES Trade(EmpId),
  FOREIGN KEY (BillID) REFERENCES Bill(BillID),
);
```

```SQL
CREATE TABLE IF NOT EXISTS Manufact (
  EmpId char(15) NOT NULL,
  ItemId char(15) NOT NULL,
  ManufactureDate Date NOT NULL,
  CostOfGoods int DEFAULT 0,
  FOREIGN KEY (EmpId) REFERENCES Trade(EmpId),
  FOREIGN KEY (ItemId) REFERENCES Items(ItemId),
  CONSTRAINT check_cost CHECK (
    CostOfGoods >= 0
  )
)
```

### 資料表結果圖

![資料表關聯圖](./document/Idef1xentityrelationshipdiagram1.png)

## 分工

呂昱諦

1. 完整性限制與詳細說明
2. 實作VIEW
3. 使用者權限劃分
4. 25%

吳枰樟

1. 設計整體架構與ER-Diagram
2. ER-Diagram轉換SQL語法
3. 完整性限制實作
4. 25%

俞漢威

1. 使用案例
2. 設計VIEW
3. 設計系統操作流程
4. 25%

許書和

1. 構思應用情境與系統需求說明
2. 繪製ER-Diagram
3. 改善ER-Diagram與架構
4. 25%
