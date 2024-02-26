// 引入FromRow特性，使我們的結構體能夠從資料庫查詢中自動解析。
use sqlx::FromRow;
use serde:: {Serialize, Deserialize};

#[derive(FromRow, Serialize)]
pub struct RoastedBean {
    pub id: i32,
    pub name: String,
    pub origin: String,
    pub roast: String,
    // 使用Option來表示這個字段可以為NULL
    pub description: Option<String>,
    pub quantity: i32,
}

#[derive(Deserialize)]
pub struct CreatRoastedBean {
    pub name: String,
    pub origin: String,
    pub roast: String,
    pub description: Option<String>,
    pub quantity: i32,
}