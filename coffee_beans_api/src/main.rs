
// 引入Axum庫中必要的組件：Router用於路由請求，get用於處理GET請求。
use axum::{
    extract::Extension,
    Json,
    routing::{get, post},
    Router,
    extract::Json as JsonExtractor,
};
use dotenv::dotenv;
use sqlx::{postgres::PgPoolOptions, types::Json};
use sqlx::PgPool;

mod model;
use model::{CreatRoastedBean, RoastedBean};

// 引入Tokio，Rust的異步運行時，這裡用於運行我們的異步主函數和TCP服務器。
#[tokio::main]
async fn main() {
    // 加載.env文件中的環境變量
    dotenv().ok();

    let database_url = std::env::var("DATABASE_URL").expect("DATABASE_URL must be set");
    let db_pool = PgPoolOptions::new()
        .connect(&database_url)
        .await
        .expect("Failed to connect to database");

    // 創建一個路由器，並為根路徑（"/"）設置一個GET請求的處理函數`hello_world`。
    let app = Router::new()
        .route("/", get(hello_world))
        .route("/beans", get(list_roasted_beans))
        .route("/beans", post(create_roasted_bean))
        .layer(Extension(db_pool));

    // 使用Tokio的TCP監聽器來綁定特定的IP地址和端口（這裡是本機地址127.0.0.1的3000端口）。
    // `.await`確保這個操作異步完成，並且`unwrap()`用於處理可能的錯誤（在這裡是直接崩潰，如果有錯誤的話）。
    let listener = tokio::net::TcpListener::bind("127.0.0.1:3000").await.unwrap();

    // 使用Axum的`serve`函數來運行服務器，這裡將之前創建的TCP監聽器和應用（app）傳入。
    // 這個`serve`函數負責處理進來的連接，並將它們分派到我們的應用程序。
    // 同樣地，使用`.await`等待服務器運行過程的異步完成，並用`unwrap()`處理可能的錯誤。
    axum::serve(listener, app).await.unwrap();
}

// 定義一個異步函數`hello_world`作為GET請求的處理函數。
// 當用戶訪問根路徑（"/"）時，這個函數將被調用，返回一個靜態字符串"Hello, World!"。
async fn hello_world() -> &'static str {
    "Hello, World!"
}

async fn list_roasted_beans(Extension(db_pool): Extension<PgPool>) -> Json<Vec<RoastedBean>> {
    let beans = sqlx::query_as::<_, RoastedBean>(
        "SELECT * FROM roasted_beans"
    )
    .fetch_all(&db_pool).await.expect("Failed to query beans");

    Json(beans)
}

async fn create_roasted_bean(JsonExtractor(payload): JsonExtractor<CreatRoastedBean>, Extension(db_pool): Extension<PgPool>) -> Json<RoastedBean> {
    let record = sqlx::query_as!(
        RoastedBean,
        "INSERT INTO roasted_beans (name, origin, roast, description, quantity) VALUES ($1, $2, $3, $4, $5) RETURNING *",
        payload.name, payload.origin, payload.roast, payload.description, payload.quantity
    )
    .fetch_one(&db_pool).await.expect("Failed to insert bean");

    Json(record)
}

