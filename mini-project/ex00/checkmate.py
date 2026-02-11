def parse_board(board_str):
    count_K = board_str.count('K') # King
    count_B = board_str.count('B') # Bishop
    count_R = board_str.count('R') # Rook
    count_Q = board_str.count('Q') # Queen
    count_P = board_str.count('P') # Pawn
    
    if count_K != 1 or count_Q > 1 or count_B > 2 or count_R > 2 or count_P > 8: #เช็คจำนวน
        return False
    
    rows = board_str.strip().split('\n')
    board = [list(row) for row in rows]
    
    if len(board)>8 or any(len(row)>8 for row in board): #เช็คจำนวนแถวและคอลัมน์ไม่เกิน 8
        return False
    if any(len(row) != len(board[0]) for row in board): #เช็คความยาวของแต่ละแถวต้องเท่ากัน
        return False
    
    return board , [count_K, count_B, count_R, count_Q, count_P]

def find_position(board,piece):
    positions = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == piece:
                positions.append((row, col))
    return positions

def map_range_position(row_range, column_range):
    position = []
    for r in row_range:
        for c in column_range:
            position.append((r,c))
    return position

def find_king_playing_positions(position_row_k,position_col_k,row_board,col_board):
    # กำหนดช่วงที่ king สามารถเล่นได้
    king_row_range = range(position_row_k-1, position_row_k+2)
    king_column_range = range(position_col_k-1, position_col_k+2)
    
    # กำหนดช่วงของกระดาน
    board_row_range = range(0, row_board)
    board_column_range = range(0, col_board)
    
    king_playing_position = map_range_position(king_row_range, king_column_range)
    king_playing_position.remove((position_row_k,position_col_k)) #เอาตำแหน่งของ king ออก
    
    board_position = map_range_position(board_row_range, board_column_range)
    
    # นำตำแหน่งของ king มาเช็คในบอร์ด เพื่อลบค่าตำแหน่งบางตัวที่ไม่ได้อยู่ในบอร์ดจริง
    valid_king_playing_position = [
        pos for pos in king_playing_position
        if pos in board_position 
    ]
    return valid_king_playing_position

def find_rook_attacking_positions(rooks_positions, row_board, col_board):
    rook_attacking_positions = []
    for row_position_rook , col_position_rook in rooks_positions:
        rook_row_range = range(0, row_board)
        rook_column_range = range(0, col_board)
        
        rook_atk_pos = map_range_position(rook_row_range, [col_position_rook]) + map_range_position([row_position_rook], rook_column_range)
        rook_attacking_positions.extend(rook_atk_pos)
    
    #clean rook_attacking_positions from list of set to single set
    rook_attacking_positions = list(set(rook_attacking_positions))
    #remove the position of rook itself
    valid_rook_attacking_positions = [
        pos for pos in rook_attacking_positions
        if pos not in rooks_positions
    ]
    return valid_rook_attacking_positions

def find_pawn_attacking_positions(pawn_positions,row_board,col_board):
    pawn_attacking_positions = []
    for row_position_pawn , col_position_pawn in pawn_positions:
        pawn_attacking_positions.extend([(row_position_pawn-1, col_position_pawn-1), (row_position_pawn-1, col_position_pawn+1)])
    
    # กำหนดช่วงของกระดาน
    board_row_range = range(0, row_board)
    board_column_range = range(0, col_board)
    
    board_position = map_range_position(board_row_range, board_column_range)
    
    valid_pawn_attacking_positions = [
        pos for pos in pawn_attacking_positions
        if pos in board_position and pos not in pawn_positions
    ]
    return valid_pawn_attacking_positions

def find_bishop_attacking_positions(bishop_positions, row_board, col_board):
    bishop_attacking_positions = []
    direction = [(-1,-1), (-1,1), (1,-1), (1,1)] #top-left, top-right, bottom-left, bottom-right
    for row_position_bishop , col_position_bishop in bishop_positions:
        for x,y in direction:
            for i in range(1, max(row_board, col_board)):
                if 0 <= row_position_bishop + x*i < row_board and 0 <= col_position_bishop + y*i < col_board:
                    move = (row_position_bishop + x*i, col_position_bishop + y*i)
                    bishop_attacking_positions.append(move)
                else:
                    break
    
    board_row_range = range(0, row_board)
    board_column_range = range(0, col_board)
    
    board_position = map_range_position(board_row_range, board_column_range)
    
    valid_bishop_attacking_positions = [
        pos for pos in bishop_attacking_positions
        if pos in board_position and pos not in bishop_positions
    ]
    return valid_bishop_attacking_positions

def find_queen_attacking_positions(queen_positions, row_board, col_board):
    queen_attacking_positions = []
    direction = [(-1,-1), (-1,1), (1,-1), (1,1), (-1,0), (1,0), (0,-1), (0,1)]
    for row_position_queen , col_position_queen in queen_positions:
        for x,y in direction:
            for i in range(1, max(row_board, col_board)):
                if 0 <= row_position_queen + x*i < row_board and 0 <= col_position_queen + y*i < col_board:
                    move = (row_position_queen + x*i, col_position_queen + y*i)
                    queen_attacking_positions.append(move)
                else:
                    break
    
    board_row_range = range(0, row_board)
    board_column_range = range(0, col_board)
    
    board_position = map_range_position(board_row_range, board_column_range)
    
    valid_queen_attacking_positions = [
        pos for pos in queen_attacking_positions
        if pos in board_position and pos not in queen_positions
    ]
    return valid_queen_attacking_positions

def check_king_position_walking_left(king_playing_positions, attack_positions):
    safe_position = []
    for pos in king_playing_positions:
        if pos not in attack_positions:
            safe_position.append(pos)
    if len(safe_position) > 0:
        return True, safe_position
    else:
        return False, safe_position

def check(king_position, attack_positions):
    if king_position in attack_positions:
        return True
    return False

def checkmate(board):
    if parse_board(board) is False:
        print("The board is not valid")
    else:
        print("Chess Board 2D Array\n")
        chess_board_2D , counts_piece = parse_board(board) # king index 0 , bishop index 1 , rook index 2 , queen index 3 , pawn index 4 for counts_piece
        
        print(list(map(str, range(len(chess_board_2D[0])))), "| <- column index")
        print("-"*len(chess_board_2D[0])*6)
        for index,row in enumerate(chess_board_2D):
            print(row, "| ", index)
        
        #find king position
        position_row_K, position_col_K = find_position(chess_board_2D, 'K')[0]
        king_playing_positions = find_king_playing_positions(position_row_K,position_col_K,len(chess_board_2D),len(chess_board_2D[0]))
        print("\n\nKing playing position:", king_playing_positions)
        print("King position:", (position_row_K, position_col_K))
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        
        attack_positions = []
        
        if counts_piece[1]>0:
            #find bishop position
            bishop_positions = find_position(chess_board_2D, 'B')
            bishop_attacking_positions = find_bishop_attacking_positions(bishop_positions, len(chess_board_2D), len(chess_board_2D[0]))
            attack_positions.extend(bishop_attacking_positions)
            print("Bishop Attacking positions:", bishop_attacking_positions)
            print("Bishop positions:", bishop_positions)
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        
        if counts_piece[2]>0:
            #find rook position
            rook_positions = find_position(chess_board_2D, 'R')
            rook_attacking_positions = find_rook_attacking_positions(rook_positions, len(chess_board_2D), len(chess_board_2D[0]))
            attack_positions.extend(rook_attacking_positions)
            print("Rook Attacking positions:", rook_attacking_positions)
            print("Rook positions:", rook_positions)
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            
        if counts_piece[3]>0:
            #find queen position
            queen_positions = find_position(chess_board_2D, 'Q')
            queen_attacking_positions = find_queen_attacking_positions(queen_positions, len(chess_board_2D), len(chess_board_2D[0]))
            attack_positions.extend(queen_attacking_positions)
            print("Queen Attacking positions:", queen_attacking_positions)
            print("Queen positions:", queen_positions)
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        
        if counts_piece[4]>0:
            #find pawn position
            pawn_positions = find_position(chess_board_2D, 'P')
            pawn_attacking_positions = find_pawn_attacking_positions(pawn_positions, len(chess_board_2D), len(chess_board_2D[0]))
            attack_positions.extend(pawn_attacking_positions)
            print("Pawn Attacking positions:", pawn_attacking_positions)
            print("Pawn positions:", pawn_positions)
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            
            
        attack_positions = list(set(attack_positions)) #clean attack_position from list of set to single set
        
        print("all attack positions:", attack_positions)
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        
###########################################################################################################################################################################
        #Check if king is in check
        is_in_check = check((position_row_K, position_col_K), attack_positions)
        print("Check?:",end="")
        print("Success" if is_in_check else "Fail")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

###########################################################################################################################################################################
        #Check mate function
        is_safe, safe_position = check_king_position_walking_left(king_playing_positions, attack_positions)
        
        for sp in safe_position:
            check_status = check(sp, attack_positions)
            if check_status:
                safe_position.remove(sp)
        
        if(len(safe_position) == 0):
            is_safe = False

        print("check mate?", not is_safe)
        print("safe position for king to walk:", safe_position)
        
        if is_safe:
            print("Not Checkmate!")
        else:
            print("Checkmate!")