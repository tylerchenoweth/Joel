from huggingface_hub import snapshot_download

model_name = "deepseek-ai/DeepSeek-R1"  # or another version
snapshot_download(repo_id=model_name, local_dir="deepseek_model")
