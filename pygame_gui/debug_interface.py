from typing import Optional

import pygame

from pygame_gui.core.interfaces import IUIManagerInterface
from pygame_gui.elements import UIWindow, UIButton

class DebugWindow(UIWindow):
    def __init__(self,
                 rect: pygame.Rect,
                 manager: Optional[IUIManagerInterface] = None):
        super().__init__(rect, manager,
                         window_display_title="pygame-gui.debug_window_title_bar",
                         element_id=['debug_window'],
                         resizable=True)
        
        self.print_layer_debug_button = UIButton(relative_rect=pygame.Rect(10, 10, -1, 30),
                                                 text='pygame-gui.print_layer_debug',
                                                 manager=self.ui_manager,
                                                 container=self,
                                                 object_id='#print_layer_debug_button',
                                                 anchors={'left': 'left',
                                                          'right': 'left',
                                                          'top': 'top',
                                                          'bottom': 'top'},
                                                 command=lambda:self.ui_manager.print_layer_debug())
        
        self.print_element_tree_button = UIButton(relative_rect=pygame.Rect(10, 40, -1, 30),
                                                 text='pygame-gui.print_layer_debug',
                                                 manager=self.ui_manager,
                                                 container=self,
                                                 object_id='#print_layer_debug_button',
                                                 anchors={'left': 'left',
                                                          'right': 'left',
                                                          'top': 'top',
                                                          'bottom': 'top'},
                                                 command=lambda:self.print_element_tree())
        
        self.open_element_info_button = UIButton(relative_rect=pygame.Rect(10, 70, -1, 30),
                                                 text='pygame-gui.print_layer_debug',
                                                 manager=self.ui_manager,
                                                 container=self,
                                                 object_id='#print_layer_debug_button',
                                                 anchors={'left': 'left',
                                                          'right': 'left',
                                                          'top': 'top',
                                                          'bottom': 'top'},
                                                 command=lambda:self.open_element_info())
        
    def print_element_tree(self):
        for element in self.ui_manager.get_root_container():
            print(element)
            
    def open_element_info(self, element):
        ElementInfoWindow(element, self.rect, self.ui_manager)

    def process_event(self, event: pygame.event.Event) -> bool:
        handled = super().process_event(event)
        
class ElementInfoWindow(UIWindow):
    def __init__(self,
                 element,
                 rect: pygame.Rect,
                 manager: Optional[IUIManagerInterface] = None,):
        super().__init__(rect, manager,
                         window_display_title="",
                         element_id=['element_info_window'],
                         resizable=True)
        self.element = element