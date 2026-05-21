# Project-local uv + Python. Source from repo root: source env.sh
export ROOT="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
export PATH="$ROOT/.local/bin:$ROOT/.venv/bin:$PATH"
export UV_CONFIG_DIR="$ROOT/.local/config/uv"
export UV_CACHE_DIR="$ROOT/.local/cache/uv"
export UV_PYTHON_INSTALL_DIR="$ROOT/.local/share/python"
export VIRTUAL_ENV="$ROOT/.venv"
