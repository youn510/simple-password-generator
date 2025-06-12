import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # ttk: themed Tkinter, 더 현대적인 위젯
import random
import string # 문자열 상수 (알파벳, 숫자 등) 제공

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("간단한 암호 생성기")
        master.geometry("400x400") # 창 크기 설정
        master.resizable(False, False) # 창 크기 조절 불가

        # 비밀번호 길이 설정 프레임
        self.length_frame = tk.LabelFrame(master, text="비밀번호 길이", padx=10, pady=10)
        self.length_frame.pack(pady=10, padx=20, fill="x")

        self.length_var = tk.IntVar(value=12) # 기본 길이 12자
        self.length_label = tk.Label(self.length_frame, text=f"길이: {self.length_var.get()}자", font=("맑은 고딕", 10))
        self.length_label.pack(side="left", padx=5)

        self.length_scale = ttk.Scale(self.length_frame, from_=8, to=32, orient="horizontal",
                                       variable=self.length_var, command=self.update_length_label)
        self.length_scale.pack(side="left", expand=True, fill="x", padx=5)

        # 포함 문자 유형 설정 프레임
        self.char_type_frame = tk.LabelFrame(master, text="포함할 문자 유형", padx=10, pady=10)
        self.char_type_frame.pack(pady=10, padx=20, fill="x")

        self.include_uppercase = tk.BooleanVar(value=True) # 기본값 True
        self.include_lowercase = tk.BooleanVar(value=True) # 기본값 True
        self.include_digits = tk.BooleanVar(value=True)    # 기본값 True
        self.include_special = tk.BooleanVar(value=False)  # 기본값 False

        ttk.Checkbutton(self.char_type_frame, text="대문자 (A-Z)", variable=self.include_uppercase).pack(anchor="w")
        ttk.Checkbutton(self.char_type_frame, text="소문자 (a-z)", variable=self.include_lowercase).pack(anchor="w")
        ttk.Checkbutton(self.char_type_frame, text="숫자 (0-9)", variable=self.include_digits).pack(anchor="w")
        ttk.Checkbutton(self.char_type_frame, text="특수 문자 (!@#$%^&*...)", variable=self.include_special).pack(anchor="w")

        # 비밀번호 생성 버튼
        self.generate_button = ttk.Button(master, text="비밀번호 생성", command=self.generate_password)
        self.generate_button.pack(pady=15)

        # 생성된 비밀번호 표시
        self.password_display = tk.Entry(master, width=40, font=("맑은 고딕", 12), justify='center', state='readonly',
                                          readonlybackground="lightgray", fg="black")
        self.password_display.pack(pady=10, padx=20)

        # 복사 버튼
        self.copy_button = ttk.Button(master, text="클립보드에 복사", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=5)

    def update_length_label(self, val):
        # 슬라이더 값이 변경될 때마다 라벨 업데이트
        self.length_label.config(text=f"길이: {int(float(val))}자")

    def generate_password(self):
        length = self.length_var.get()
        characters = ""
        
        if self.include_uppercase.get():
            characters += string.ascii_uppercase # A-Z
        if self.include_lowercase.get():
            characters += string.ascii_lowercase # a-z
        if self.include_digits.get():
            characters += string.digits         # 0-9
        if self.include_special.get():
            characters += string.punctuation    # !@#$%^&* 등

        if not characters:
            messagebox.showwarning("경고", "비밀번호에 포함할 문자 유형을 최소 하나 이상 선택해야 합니다.")
            self.password_display.config(state='normal') # 일시적으로 쓰기 가능으로 변경
            self.password_display.delete(0, tk.END)
            self.password_display.config(state='readonly') # 다시 읽기 전용으로 변경
            return

        # 선택된 문자 유형에서 최소한 하나씩은 포함되도록 보장
        password_chars = []
        if self.include_uppercase.get():
            password_chars.append(random.choice(string.ascii_uppercase))
        if self.include_lowercase.get():
            password_chars.append(random.choice(string.ascii_lowercase))
        if self.include_digits.get():
            password_chars.append(random.choice(string.digits))
        if self.include_special.get():
            password_chars.append(random.choice(string.punctuation))

        # 나머지 길이를 채우기 위해 전체 문자 세트에서 무작위 선택
        if len(password_chars) < length: # 보장된 문자 수가 전체 길이보다 짧을 경우
            remaining_length = length - len(password_chars)
            password_chars.extend(random.choice(characters) for _ in range(remaining_length))

        random.shuffle(password_chars) # 비밀번호 문자열 섞기
        generated_password = "".join(password_chars)

        self.password_display.config(state='normal') # 읽기 전용 해제
        self.password_display.delete(0, tk.END) # 기존 내용 삭제
        self.password_display.insert(0, generated_password) # 새 비밀번호 삽입
        self.password_display.config(state='readonly') # 다시 읽기 전용 설정

    def copy_to_clipboard(self):
        password = self.password_display.get()
        if password:
            self.master.clipboard_clear() # 클립보드 비우기
            self.master.clipboard_append(password) # 비밀번호 복사
            messagebox.showinfo("복사 완료", "비밀번호가 클립보드에 복사되었습니다!")
        else:
            messagebox.showwarning("경고", "생성된 비밀번호가 없습니다.")

# Tkinter 윈도우 생성 및 앱 시작
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()