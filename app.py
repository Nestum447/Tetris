import streamlit as st
import time

# Constantes
ROWS = 20
COLS = 10
EMPTY = "⬛"
BLOCK = "🟦"

# Inicializa el tablero vacío
def init_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

# Dibuja el tablero como string con emojis
def draw_board(board):
    return '\n'.join([''.join(row) for row in board])

# Simula caída de pieza vertical
def drop_piece(board, col):
    for row in range(ROWS):
        if row > 0:
            board[row - 1][col] = EMPTY
        board[row][col] = BLOCK
        st.code(draw_board(board))
        time.sleep(0.1)
        if row < ROWS - 1:
            board[row][col] = EMPTY

# --- Streamlit UI ---
st.set_page_config(page_title="Tetris Visual", layout="centered")
st.title("Tetris Simple (Visual con Emojis)")

if "board" not in st.session_state:
    st.session_state.board = init_board()

col = st.slider("Selecciona columna de caída (0 a 9)", 0, COLS - 1, COLS // 2)

if st.button("Soltar pieza"):
    st.session_state.board = init_board()
    drop_piece(st.session_state.board, col)
