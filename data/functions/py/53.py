def lstm_area_attention_base():
  """Hparams for LSTM with area attention."""
  hparams = lstm_luong_attention()
  hparams.batch_size = 16384
  hparams.num_hidden_layers = 2
  hparams.hidden_size = 1024
  hparams.num_heads = 4
  hparams.dropout = 0.2
  hparams.learning_rate = 0.1
  hparams.max_area_width = 2
  hparams.area_key_mode = "mean"
  hparams.area_value_mode = "sum"
  return hparams