use serde::{Deserialize, Serialize};

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct SummarizeRowResponse {
  pub text: String,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct TranslateRowResponse {
  text: String,
}
