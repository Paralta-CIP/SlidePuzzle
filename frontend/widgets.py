import pygame


class Widgets:
    """
    Small pygame widgets like title and buttons.
    """

    def __init__(self, screen: pygame.Surface, font_path: str):
        self.screen = screen
        self.font_path = font_path

    def draw_line(self, line_position: int, height: int):
        """
        A split line between puzzle and buttons.
        """
        pygame.draw.line(self.screen, 'black', (line_position, 0), (line_position, height), 2)

    def draw_title(self, title_center: tuple[int, int], title_size: int):
        font = pygame.font.Font(self.font_path, title_size)
        title = font.render("拼图华容道", True, 'black')
        title_rect = title.get_rect()
        title_rect.center = title_center
        self.screen.blit(title, title_rect)

    def draw_selection(self, selection_center: tuple[int, int], selection_size: int):
        """
        Image selection button.
        """
        button_rect = pygame.Rect((0, 0, 4 * selection_size + 20, selection_size + 20))
        button_rect.center = selection_center
        pygame.draw.rect(self.screen, 'grey', button_rect)
        pygame.draw.rect(self.screen, 'black', button_rect, 2)

        font = pygame.font.Font(self.font_path, selection_size)
        text = font.render("选择图像", True, 'black')
        text_rect = text.get_rect()
        text_rect.center = selection_center
        self.screen.blit(text, text_rect)

        return button_rect

    def draw_start(self, start_center: tuple[int, int], start_size: int):
        """
        Start button.
        """
        button_rect = pygame.Rect((0, 0, 2 * start_size + 20, start_size + 20))
        button_rect.center = start_center

        pygame.draw.rect(self.screen, 'black', button_rect, 2)
        font = pygame.font.Font(self.font_path, start_size)
        text = font.render("开始", True, 'black')
        text_rect = text.get_rect()
        text_rect.center = start_center
        self.screen.blit(text, text_rect)

        return button_rect

    def draw_complete(self, complete_center: tuple[int, int], complete_size: int):
        """
        Puzzle-completion text.
        """
        font = pygame.font.Font(self.font_path, complete_size)
        text = font.render("成功复原!", True, (34, 139, 34))
        text_rect = text.get_rect()
        text_rect.center = complete_center
        self.screen.blit(text, text_rect)

    def erase_complete(self, complete_center: tuple[int, int], complete_size: int):
        """
        Erase the puzzle-completion text.
        """
        erase_rect = pygame.Rect(0, 0, complete_size * 5, complete_size)
        erase_rect.center = complete_center
        pygame.draw.rect(self.screen, 'white', erase_rect)
