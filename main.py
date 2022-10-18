import pygame
import sys
import chessAI
import time

from const import *
from game import Game
from square import Square
from move import Move

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('ChessVsMyAI')
        self.game = Game()

    def print_text_win(self):
        font = pygame.font.SysFont("Times New Roman", 50, True, False)
        surface = font.render("You Win !!!!!!!!", True, (0, 255, 0))
        self.screen.blit(surface, (280 , 350))

    def print_text_lose(self):
        font = pygame.font.SysFont("Times New Roman", 50, True, False)
        surface = font.render("Noob Dog !!!!", True, (255, 0, 0))
        self.screen.blit(surface, (280 , 350))

    def mainloop(self):
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger
        gameboard = chessAI.setUpBoard()

        while True:
            # show methods
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)
            
            if dragger.dragging:
                dragger.update_blit(screen)

            if game.next_player == 'black':
                first, last = chessAI.studentAgent(gameboard)
                if gameboard[first][0] == 'Pawn' and last[0] == 7:
                    gameboard[last] = ('Queen', 'Black')
                else:
                    gameboard[last] = gameboard[first]
                gameboard.pop(first)
                initial = Square(first[0], first[1])
                final = Square(last[0], last[1])
                piece = board.squares[initial.row][initial.col].piece
                captured = board.squares[final.row][final.col].has_piece()
                move = Move(initial, final)
                board.move(piece, move)
                board.set_true_en_passant(piece)                            

                # sounds
                game.play_sound(captured)
                # show methods
                game.show_bg(screen)
                game.show_last_move(screen)
                game.show_pieces(screen)
                # next turn
                game.next_turn()
                pygame.display.update()
            else:
                for event in pygame.event.get():
                    # click
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        dragger.update_mouse(event.pos)

                        clicked_row = dragger.mouseY // SQSIZE
                        clicked_col = dragger.mouseX // SQSIZE
                        
                        # if clicked square has a piece ?
                        if board.squares[clicked_row][clicked_col].has_piece():
                            piece = board.squares[clicked_row][clicked_col].piece
                            
                            # valid piece (color) ?
                            if piece.color == game.next_player:
                                board.calc_moves(piece, clicked_row, clicked_col, bool=True)
                                dragger.save_initial(event.pos)
                                dragger.drag_piece(piece)
                                # show methods 
                                game.show_bg(screen)
                                game.show_last_move(screen)
                                game.show_moves(screen)
                                game.show_pieces(screen)
                    
                    # mouse motion
                    elif event.type == pygame.MOUSEMOTION:
                        motion_row = event.pos[1] // SQSIZE
                        motion_col = event.pos[0] // SQSIZE

                        game.set_hover(motion_row, motion_col)

                        if dragger.dragging:
                            dragger.update_mouse(event.pos)
                            # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                            game.show_hover(screen)
                            dragger.update_blit(screen)
                    
                    # click release
                    elif event.type == pygame.MOUSEBUTTONUP:
                        
                        if dragger.dragging:
                            dragger.update_mouse(event.pos)

                            released_row = dragger.mouseY // SQSIZE
                            released_col = dragger.mouseX // SQSIZE

                            # create possible move
                            initial = Square(dragger.initial_row, dragger.initial_col)
                            final = Square(released_row, released_col)
                            move = Move(initial, final)

                            # valid move ?
                            first = (clicked_row, clicked_col)
                            second = (released_row, released_col)
                            movezz = chessAI.findMove(gameboard[first][0], first[0], first[1], 8, 8, gameboard, 'White')
                            if gameboard[first] == 'King' and first[0] == 7 and first[1] == 4:
                                board.calc_moves()
                            if (released_row, released_col) in movezz:
                                if gameboard[first][0] == "Pawn" and released_row == 0:
                                    gameboard[(released_row, released_col)] = ("Queen", "White")
                                else:
                                    gameboard[(released_row, released_col)] = gameboard[(dragger.initial_row, dragger.initial_col)]
                                gameboard.pop((dragger.initial_row, dragger.initial_col))
                                # normal capture
                                captured = board.squares[released_row][released_col].has_piece()
                                board.move(dragger.piece, move)

                                board.set_true_en_passant(dragger.piece)                            

                                # sounds
                                game.play_sound(captured)
                                # show methods
                                game.show_bg(screen)
                                game.show_last_move(screen)
                                game.show_pieces(screen)
                                game.show_moves(screen)
                                # next turn
                                game.next_turn()
                            elif gameboard[first][0] == 'King' and  second == (7, 2) or second == (7, 6) and board.valid_move(dragger.piece, move):
                                # normal capture
                                if second == (7, 2):
                                    gameboard[second] = gameboard[first]
                                    gameboard[(7, 3)] = ("Rook", "White")
                                    gameboard.pop((7, 0))
                                else:
                                    gameboard[second] = gameboard[first]
                                    gameboard[(7, 5)] = ("Rook", "White")
                                    gameboard.pop((7, 7))
                                gameboard.pop(first)
                                captured = board.squares[released_row][released_col].has_piece()
                                board.move(dragger.piece, move)

                                board.set_true_en_passant(dragger.piece)                            

                                # sounds
                                game.play_sound(captured)
                                # show methods
                                game.show_bg(screen)
                                game.show_last_move(screen)
                                game.show_pieces(screen)
                                # next turn
                                game.next_turn()
                        dragger.undrag_piece()
                    
                    # key press
                    elif event.type == pygame.KEYDOWN:
                        
                        # changing themes
                        if event.key == pygame.K_t:
                            game.change_theme()

                        # changing themes
                        if event.key == pygame.K_r:
                            game.reset()
                            game = self.game
                            board = self.game.board
                            dragger = self.game.dragger

                    # quit application
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    game.show_pieces(screen) 
                pygame.display.update()
                if ('King', 'Black') not in gameboard.values():
                    self.print_text_win()
                    time.sleep(2)
                    break
                elif ('King', 'White') not in gameboard.values():
                    self.print_text_lose()
                    pygame.display.update()
                    time.sleep(2)
                    break
                
main = Main()
main.mainloop()