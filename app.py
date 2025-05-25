import streamlit as st
import time

ROWS, COLS = 20, 10
EMPTY = "⬛"
BLOCK = "🟦"
I_SHAPE = [(0, 0), (1, 0), (2, 0), (3, 0)]  # pieza vertical

def init_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def draw_board(board):
    return '\n'.join([''.join(row) for row in board])

def place_piece(board, shape, pos, value):
    for r, c in shape:
        y, x = pos[0] + r, pos[1] + c
        if 0 <= y < ROWS and 0 <= x < COLS:
            board[y][x] = value

def check_collision(board, shape, pos):
    for r, c in shape:
        y, x = pos[0] + r, pos[1] + c
        if y >= ROWS or x < 0 or x >= COLS or (y >= 0 and board[y][x] == BLOCK):
            return True
    return False

def fix_piece():
    place_piece(st.session_state.board, st.session_state.piece, st.session_state.pos, BLOCK)

def new_piece():
    st.session_state.piece = I_SHAPE
    st.session_state.pos = [0, 3]

# Inicializa el juego
if "board" not in st.session_state:
    st.session_state.board = init_board()
    new_piece()

# Tablero temporal para mostrar la pieza actual
temp_board = [row.copy() for row in st.session_state.board]
place_piece(temp_board, st.session_state.piece, st.session_state.pos, BLOCK)
st.code(draw_board(temp_board))

# --- CONTROLES ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("◀️ Izquierda"):
        new_pos = [st.session_state.pos[0], st.session_state.pos[1] - 1]
        if not check_collision(st.session_state.board, st.session_state.piece, new_pos):
            st.session_state.pos = new_pos

with col2:
    if st.button("▶️ Derecha"):
        new_pos = [st.session_state.pos[0], st.session_state.pos[1] + 1]
        if not check_collision(st.session_state.board, st.session_state.piece, new_pos):
            st.session_state.pos = new_pos

with col3:
    if st.button("⬇️ Abajo"):
        new_pos = [st.session_state.pos[0] + 1, st.session_state.pos[1]]
        if check_collision(st.session_state.board, st.session_state.piece, new_pos):
            fix_piece()
            new_piece()
        else:
            st.session_state.pos = new_pos

with col4:
    if st.button("🔄 Reiniciar"):
        st.session_state.board = init_board()
        new_piece()
