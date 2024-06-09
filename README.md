<!-- Version description:
  This version contains "Client" entity with extended relationships.
-->

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
  - [資料舉例](#資料舉例)
  - [Schema](#schema)
  - [SQL](#sql)
    - [資料表結果圖](#資料表結果圖)
  - [分工](#分工)
  - [參考資料](#參考資料)

## 應用情境

作為礦業開發公司所使用的會計系統,
本系統資料庫涵蓋材料、存貨、訂單、物品之儲存,
可延伸之應用為訂單、存貨、貿易、會計、管理系統等。

礦業進行開發時,採集到之天然礦物將作為存貨儲存至存貨資料庫。
而礦業開發所運用到之各項器具、物品等,將儲存至材料資料庫中。
會計系統將以存貨、銷售、與進貨產生的付款收款明細來結算交易。

## 系統需求說明

本系統將存貨、材料或裝置等以物品ID、名稱、存放地、類別、數量
、單價、供應商、用途與購置日期等,儲存至物品資料表。
其中,存貨無需紀錄供應商、購置日期。員工資料表將儲存員工ID、員工姓名、所屬部門與其職位。

採購部門進貨時,交易訂單應紀錄交易類別、負責員工ID、物品ID、
交易對象、訂單編號、付款方式與付款日期,
且以交易類別來區分銷售部門訂單區分。
銷售部門賣出存貨時,應紀錄之項目如採購部門相同,並透過交易類別區分採購訂單。

生產部門儲存商品時,應紀錄負責員工ID、物品ID、銷貨成本與製造日期,
此處物品單價意指商品售價。

會計系統將收付款明細結算交易時,應紀錄專責員工ID與帳單編號。
收付款明細將紀錄帳單編號、訂單編號、交易日期、銀行代碼、銀行帳號、銀行名稱、交易對象與金額。

## 使用案例

### 使用案例圖

![Use case diagram](./document/Usecase.png)

## 完整性限制

員工

1. 員工ID:長度為11的大寫英數字串,不可為空,格式為 `DEP-POS-ID`
   1. 三個部分以 `-` 符號分隔,字母皆為大寫。
   2. `DEP` 代表部門,以1至3位大寫英文字母編碼。
   3. `POS` 代表職位,以1至3位大寫英文字母編碼。
   4. `ID` 為3位大寫英文字母與數字編碼。
   5. 縮寫舉例列於 [詳細說明](#詳細說明)
2. 部門:長度為10的中文字串,須符合公司內的部門名稱,不可為空。
3. 職位:長度為10的中文字串,須符合公司內的職位名稱,不可為空。
4. 姓名:長度為10的中文字串,須符合姓氏+名字順序,不可為空。

銀行
<!-- TODO: Check the length whether "7" or "3 to 7" -->
1. 銀行代碼:長度為3或7的數字串,不可為空。
   1. 格式為 `金融機構總代號` `分支機構代號`,皆可由`0`開頭。
   2. `金融機構總代號` 為3碼數字
   3. `分支機構代號` 為4碼數字
   4. `金融機構總代號` 可單獨存在，`分支機構代號`必須接在其後。
   5. `金融機構總代號` 與 `分支機構代號` 同時存在時，中間不須連接符號
   6. 驗證是否為合法來源: [財金資訊股份有限公司 總分支機構查詢](https://www.fisc.com.tw/TC/Service?CAID=51254999-5d15-4ddf-8e54-4b2cdb2a8399)
2. 銀行名稱:長度為30的中文字串，不可為空。
   1. 需為中華民國登記在案的銀行名稱。
   2. 參考來源: [財金資訊股份有限公司 總分支機構查詢](https://www.fisc.com.tw/TC/Service?CAID=51254999-5d15-4ddf-8e54-4b2cdb2a8399)

客戶

1. 客戶ID:長度為10的大寫英數字串, 格式為 `Client-ID`, 不可為空。
   2. `Client` 為6個字元之大寫字母 `CLIENT`
   3. 第八個字元為 `-`
   4. `ID` 為長度三且隨機的大寫英數字串, `[A-Z0-9]{3}`
2. 客戶名稱:長度為40的字串, 不可為空
   1. 考慮可能為法人(公司)而設定此長度

供應商

1. 供應商ID:長度為6的大寫英數字串, 格式為 `Supplier-ID`, 不可為空
   1. `Supplier` 為三個大寫字母`SUP`
   2. 第四個字元為 `-`
   3. `ID` 為長度二且隨機的大寫英數字串, `[A-Z0-9]{2}`
2. 供應商名稱:長度為50的中文字串, 不可為空
   1. 需符合登記在經濟部公司法人名稱

物品類別

1. 物品類別ID:長度為7的大寫英數字串，格式為 `CAT-No`, 不可為空
   1. 兩個部分 `CAT` 與 `itmeID` 之間以 `-` 字元分隔
   2. `CAT` 為固定的三個大寫字母：CAT
   3. `No` 為隨機三位整數，由程式產生。
2. 類別說明, 不可為空
   1. 長度為10的中文字串,如礦石類、工具類、材料類,預設值為未分類。

倉庫

1. 倉庫ID:長度為7的大寫英數字串，格式為 `WH-1000`,不可為空。
   1. 前2個字元固定為 `WH`
   2. 第3個字元為 `-` 作為分隔符號
   3. 後四個字元為數字,`0001`至 `9999`
2. 倉庫地址:不超過70字元字串，格式為 `縣市-鄉鎮市區-村里-道路街名-巷-弄-號-樓-室`，不可為空。
3. 倉庫備註:不超過100字元字串，可為空。

物品

1. 物品ID:長度為15的大寫英數字串, 不可為空
   1. `[A-Z]{5}[0-9]{10}`
   2. 前五碼為大寫英文AAAAA~ZZZZZ
   3. 後十碼為正整數0000000000~9999999999。
2. 物品類別ID:長度為7的字串，格式為 `CAT-No`, 參考 `物品類別ID`
3. 物品名稱:長度為50的中文字串,不可為空。
4. 物品數量:正浮點數,不可為空,預設值為0.0。
   1. 若物品類別無法以個數計數時，單位為公斤
   2. 物品數量單位不另外分類與紀錄
5. 數量單位:四個字元的字串，只可為以下字串。不可為空。
   1. "公斤"、"公尺"、"立方公尺"、"平方公尺"、"個"、"單位"。
   2. 對應物品類別選擇適當的單位。
6. 物品單價:正整數,不可為空,預設值為0。
7. 用途:長度為50的中文字串,可為空,預設值為NULL。
8. 存放地點:長度為7的字串，參考`倉庫之倉庫ID`,不可為空。
9. 購置日期:只儲存年月日,不得小於從公司建立日期,預設值為NULL。
   1. 格式為 `yyyy/MM/dd`
10. 供應商:長度為6的字串, 參考`供應商之供應商ID`,不可為空。

收付款明細

1. 帳單編號:長度為10的字母與數字,不可為空。格式如下。
   1. `^[A-Za-z0-9]{3}-\d{6}$`
   2. 前3碼為隨機的英文字母及數字
   3. 第4碼為字元"-"
   4. 後6碼為隨機的數字
2. 訂單編號:長度為12的字串,參考`交易關係之訂單編號`,格式為 `DATE-OrderId`。
   1. `DATE` 為下單日期, 長度為8的數字字串, 格式為 `YYYYMMDD`, 紀錄年月日
   2. 第9碼為字元 `-`
   3. `OrderId` 為3碼隨機, 包含大小寫的英文字母及數字
3. 交易對象:長度為10的字串, 參考 `客戶之客戶ID`, 不可為空
4. 銀行代碼:長度為3的字串, 參考 `銀行之銀行代碼`。
   1. 若該筆訂單非轉匯款支付，不可為空。
5. 銀行帳號:長度為14的數字字串,7+7(局號+帳號)。
   1. 若該筆訂單非轉匯款支付，不可為空。
6. 交易日期:只儲存年月日,不得小於從公司建立日期,預設值為NULL。
   1. 格式為 `yyyy/MM/dd`
7. 金額:正整數,不可為空

交易關係

1. 訂單編號:長度為12的字串,格式為 `DATE-OrderId`。
   1. `DATE` 為下單日期, 長度為8的數字字串, 格式為 `YYYYMMDD`, 紀錄年月日
   2. 第9碼為字元 `-`
   3. `OrderId` 為3碼隨機, 包含大小寫的英文字母及數字
2. 員工ID:長度為10的字串,不可為空,格式為`DEP-POS-ID`。
3. 交易類別:長度為2的字串,僅為"購入" 或"銷售",不可為空。
4. 物品ID:長度為15的字串。
5. 交易數量:正浮點數，不可為空。
   1. 對應`物品類別`，若為可數之物品，小數點後應為零。
6. 付款日期:儲存日期時間,不得小於從公司建立日期, 可為空,預設值為NULL。
   1. 格式為 `yyyy/MM/dd`
7. 付款方式:長度為2的中文字串，只可為 "匯款"或"付現"，不可為空。
8. 交易對象:長度為10的字串, 參考 `客戶之客戶ID`, 不可為空。

製造關係

1. 員工ID:長度為10的字串,不可為空,格式為`DEP-POS-ID`。
2. 物品ID:長度為15的字串,格式如前述。
3. 製造日期:儲存日期時間,可為空,不得小於從公司建立日期,預設值為輸入資料當日。
   1. 格式為 `yyyy/MM/dd`
4. 銷貨成本:正整數,包含零,預設值為NULL。

紀錄關係

1. 員工ID:長度為10的字串,不可為空,格式為`DEP-POS-ID`。
2. 帳單編號:長度為10的字母與數字。
   1. 格式為 `^[A-Za-z0-9]{3}-\d{6}$`

## ER-Diagram

共有八個實體

1. 物品
2. 員工
3. 收付款明細
4. 銀行
5. 客戶
6. 供應商
7. 物品類別
8. 倉庫

共有三個關聯

1. 交易
2. 製造
3. 紀錄

![ER-Diagram](./document/Chenerdiagram_v2.png)

### 實體屬性與關聯說明

此段僅列出實體所擁有之屬性，
說明列於[詳細說明](#詳細說明)

實體

| 實體 | 屬性   | Key         |
| ---- | ------ | ----------- |
| 員工 | 員工ID | Primary Key |
|      | 姓名   |             |
|      | 部門   |             |
|      | 職位   |             |

| 實體 | 屬性     | Key         |
| ---- | -------- | ----------- |
| 銀行 | 銀行代碼 | Primary Key |
|      | 銀行名稱 | Unique      |

| 實體 | 屬性     | Key         |
| ---- | -------- | ----------- |
| 客戶 | 客戶ID   | Primary Key |
|      | 客戶名稱 |             |

| 實體   | 屬性       | Key         |
| ------ | ---------- | ----------- |
| 供應商 | 供應商ID   | Primary Key |
|        | 供應商名稱 |             |

| 實體     | 屬性       | Key         |
| -------- | ---------- | ----------- |
| 物品類別 | 物品類別ID | Primary Key |
|          | 類別說明   |             |

| 實體 | 屬性       | Key         |
| ---- | ---------- | ----------- |
| 物品 | 物品ID     | Primary Key |
|      | 物品類別ID | Foreign Key |
|      | 物品名稱   |             |
|      | 物品數量   |             |
|      | 物品單價   |             |
|      | 用途       |             |
|      | 存放地點   | Foreign Key |
|      | 購置日期   |             |
|      | 供應商     | Foreign Key |

| 實體       | 屬性     | Key         |
| ---------- | -------- | ----------- |
| 收付款明細 | 帳單編號 | Primary Key |
|            | 訂單編號 | Foreign Key |
|            | 銀行名稱 |             |
|            | 交易對象 | Foreign Key |
|            | 銀行代碼 |             |
|            | 銀行帳號 |             |
|            | 交易日期 |             |
|            | 金額     |             |

關聯

1. 交易關係
   | 關聯 | 關聯實體 | 關聯實體 | Cardinality | 說明                                                               |
   | ---- | -------- | -------- | ----------- | ------------------------------------------------------------------ |
   | 交易 | 物品     | 員工     | 多對多      | 至少一位員工會購買工廠的器具與銷售商品，且商品一定會被購入與賣出。 |

   | 關聯 | 屬性     | Key         |
   | ---- | -------- | ----------- |
   | 交易 | 訂單編號 | Primary Key |
   |      | 物品ID   | Foreign Key |
   |      | 員工ID   | Foreign Key |
   |      | 交易類別 |             |
   |      | 交易對象 | Foreign Key |
   |      | 付款方式 |             |
   |      | 付款日期 |             |

2. 製造關係
   | 關聯 | 關聯實體 | 關聯實體 | Cardinality | 說明                                                       |
   | ---- | -------- | -------- | ----------- | ---------------------------------------------------------- |
   | 製造 | 物品     | 員工     | 一對多      | 至少一個員工會負責製造商品，且一個商品只會由一位員工負責。 |

   | 關聯 | 屬性     | Key         |
   | ---- | -------- | ----------- |
   | 製造 | 員工ID   | Foreign Key |
   |      | 物品ID   | Foreign Key |
   |      | 銷貨成本 |             |
   |      | 製造日期 |             |

3. 紀錄關係
   | 關聯 | 關聯實體 | 關聯實體   | Cardinality | 說明                                                               |
   | ---- | -------- | ---------- | ----------- | ------------------------------------------------------------------ |
   | 紀錄 | 員工     | 收付款明細 | 一對多      | 至少有一個員工會負責紀錄收付款明細，且一個明細只會由一位員工負責。 |

   | 關聯 | 屬性     | Key         |
   | ---- | -------- | ----------- |
   | 紀錄 | 員工ID   | Foreign Key |
   |      | 帳單編號 | Foreign Key |

## 詳細說明

實體

| 實體 | 屬性   | Key         | Domain                               | 說明                                                   |
| ---- | ------ | ----------- | ------------------------------------ | ------------------------------------------------------ |
| 員工 | 員工ID | Primary Key | 格式為 `DEP-POS-ID`                  | 員工的ID，`DEP` 代表部門、`POS` 代表職位、`ID`為編號。 |
|      |        |             | `^[A-Z]{1,3}-[A-Z]{1,3}-[A-Z0-9]{3}$` | 部門、職位依據員工實際資料，編號由程式產生。           |
|      | 姓名   |             | 長度為10的中文字串                   | 員工的姓名。                                           |
|      | 部門   |             | 長度為10的中文字串                   | 員工部門，該部門需存在於公司中。                       |
|      | 職位   |             | 長度為10的中文字串                   | 員工職位。                                             |

部門縮寫範例

1. `MSD`: Marketing and Sales Department, 行銷與銷售部門
2. `FD`: Finance Department, 財務部門
3. `POD`: Production/Operations Department, 生產/運營部門
4. `RDD`: Research and Development Department, 研究與開發部門
5. `CSD`: Customer Service Department, 客戶服務部門
6. `PD`: Purchasing Department, 採購部門
7. `ITD`: IT Department, 資訊科技部門

職位縮寫範例

1. `BL`: Blaster, 爆破工
2. `UM`: Underground Miner, 地下礦工
3. `HEO`: Heavy Equipment Operator, 重型設備操作員
4. `DR`: Driller, 鑽孔員
5. `EL`: Electrician, 電工
6. `MP`: Material Planner, 物料規劃員
7. `HSS`: Health and Safety Specialist, 健康與安全專員
8. `MM`: Mine Manager, 礦場經理
9. `CH`: Chemist, 化學家
10. `GE`: Geological Engineer, 地質工程師

| 實體 | 屬性     | Key     | Domain                        | 說明 |
| ---- | -------- | ------- | ----------------------------- | ---- |
| 銀行 | 銀行代碼 | Primary | 長度為7的數字字串,可由`0`開頭 |      |
|      |          |         | `^([0-9]{3}\|[0-9]{7})$`      |      |
|      | 銀行名稱 |         |                               |      |

| 實體 | 屬性 | Key | Domain | 說明 |
| ---- | ---- | --- | ------ | ---- |
| 客戶 |      |     |        |      |

| 實體   | 屬性 | Key | Domain | 說明 |
| ------ | ---- | --- | ------ | ---- |
| 供應商 |      |     |        |      |

| 實體 | 屬性     | Key | Domain | 說明                                             |
| ---- | -------- | --- | ------ | ------------------------------------------------ |
| 物品 | 物品ID   |     |        | 物品的編號，由程式產生。                         |
|      | 物品類別 |     |        | 物品的名稱。                                     |
|      | 物品名稱 |     |        | 物品類別，由類別判斷是否為商品。                 |
|      | 物品數量 |     |        | 物品數量。                                       |
|      | 物品單價 |     |        | 物品為商品時，指物品售價；否則為購入的物品單價。 |
|      | 用途     |     |        | 物品存放地點。                                   |
|      | 存放地點 |     |        | 物品之購入日期。                                 |
|      | 購置日期 |     |        | 物品之說明欄位。                                 |
|      | 供應商   |     |        | 購入物品之供應商。                               |

| 實體       | 屬性     | Key         | Domain | 說明                                                                               |
| ---------- | -------- | ----------- | ------ | ---------------------------------------------------------------------------------- |
| 收付款明細 | 帳單編號 | Primary Key |        | 紀錄收付款明細的，此編號由系統產生。                                               |
|            | 訂單編號 | Foreign Key |        | 銷售或進貨訂單上的訂單編號，此編號由系統產生。                                     |
|            | 銀行名稱 |             |        | 對應銀行代碼之銀行名稱。                                                           |
|            | 交易對象 | Foreign Key |        | 交易對象可為客戶時，指此為銷售。為本公司時，則為進貨。此欄位參考修交易的交易對象。 |
|            | 銀行代碼 |             |        | 該銀行對應的三碼數字，由程式檢查其正確性。                                         |
|            | 銀行帳號 |             |        | 銀行的帳號。                                                                       |
|            | 交易日期 |             |        | 只儲存年月日。                                                                     |
|            | 金額     |             |        | 該訂單的金額。                                                                     |

關聯

| 關聯 | 關聯實體 | 關聯實體 | Cardinality | 說明                                                               |
| ---- | -------- | -------- | ----------- | ------------------------------------------------------------------ |
| 交易 | 物品     | 員工     | 多對多      | 至少一位員工會購買工廠的器具與銷售商品，且商品一定會被購入與賣出。 |

| 關聯 | 屬性     | Key | Domain | 說明 |
| ---- | -------- | --- | ------ | ---- |
| 交易 | 訂單編號 |     |        |      |
|      | 物品ID   |     |        |      |
|      | 員工ID   |     |        |      |
|      | 交易類別 |     |        |      |
|      | 交易對象 |     |        |      |
|      | 付款方式 |     |        |      |
|      | 付款日期 |     |        |      |

| 關聯 | 關聯實體 | 關聯實體 | Cardinality | 說明                                                       |
| ---- | -------- | -------- | ----------- | ---------------------------------------------------------- |
| 製造 | 物品     | 員工     | 一對多      | 至少一個員工會負責製造商品，且一個商品只會由一位員工負責。 |

| 關聯 | 屬性     | Key | Domain | 說明 |
| ---- | -------- | --- | ------ | ---- |
| 製造 | 員工ID   |     |        |      |
|      | 物品ID   |     |        |      |
|      | 銷貨成本 |     |        |      |
|      | 製造日期 |     |        |      |

| 關聯 | 關聯實體 | 關聯實體   | Cardinality | 說明                                                               |
| ---- | -------- | ---------- | ----------- | ------------------------------------------------------------------ |
| 紀錄 | 員工     | 收付款明細 | 一對多      | 至少有一個員工會負責紀錄收付款明細，且一個明細只會由一位員工負責。 |

| 關聯 | 屬性     | Key | Domain | 說明 |
| ---- | -------- | --- | ------ | ---- |
| 紀錄 | 員工ID   |     |        |      |
|      | 帳單編號 |     |        |      |

## 資料舉例

範例資料可參考 [Reference data](./reference_data.md)

| 實體 | 屬性   | 範例資料   |
| ---- | ------ | ---------- |
| 員工 | 員工ID | PDD-PM-100 |
|      |        |            |

| 實體 | 屬性 | 範例資料 |
| ---- | ---- | -------- |
| 銀行 |      |          |

| 實體 | 屬性 | 範例資料 |
| ---- | ---- | -------- |
| 客戶 |      |          |

| 實體 | 屬性 | 範例資料 |
| ---- | ---- | -------- |
| 供應商 |      |          |

| 實體 | 屬性 | 範例資料 |
| ---- | ---- | -------- |
| 物品 |      |          |

| 實體 | 屬性 | 範例資料 |
| ---- | ---- | -------- |
|收付款明細 |      |          |

| 實體 | 屬性 | 範例資料 |
| ---- | ---- | -------- |
| 交易 |      |          |

| 實體 | 屬性 | 範例資料 |
| ---- | ---- | -------- |
| 製造 |      |          |

| 實體 | 屬性 | 範例資料 |
| ---- | ---- | -------- |
| 紀錄 |      |          |

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

## 參考資料

1. [全國營業(稅籍)登記資料集](https://data.gov.tw/dataset/9400)
