#ifndef DUMMY_H_
#define DUMMY_H_

void LCD_voidInit(void);
void LCD_voidSendCommand(u8);
void LCD_voidWriteCharacter(u8);
void LCD_voidWriteString(string);
void LCD_voidCursorPosition(u8, u8);
void LCD_voidWriteCustomCharacter(u8*, u8, u8);
void LCD_voidWriteNumber(f32, u8);

#endif