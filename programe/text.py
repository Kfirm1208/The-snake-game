def draw_text(text,font,text_col,surface,x,y):
    img = font.render(text,True,text_col)
    surface.blit(img,(x,y))        