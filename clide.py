import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import tkinter.font as tkfont
import sys
import os
import subprocess

CLIDE_VERSION = "v0.0.1"
SCRIPT_PATH = os.path.abspath(__file__)
LOGO_ICO = os.path.join(os.path.dirname(SCRIPT_PATH), "icons", "logo.ico")
COMMON_BG = "gray5"
COMMON_FONTSIZE = 16
COMMON_FONT = "Iosevka" # You can change it to your desired font

# This Section is fully done by CLAUDE as i dont know all the types 

C_TYPES = {
    "void",
    "char", "signed char", "unsigned char",
    "short", "short int", "signed short", "signed short int",
    "unsigned short", "unsigned short int",
    "int", "signed", "signed int",
    "unsigned", "unsigned int",
    "long", "long int", "signed long", "signed long int",
    "unsigned long", "unsigned long int",
    "long long", "long long int", "signed long long", "signed long long int",
    "unsigned long long", "unsigned long long int",
    "float",
    "double",
    "long double",
    "_Bool",
    "_Complex",
    "_Imaginary",
    
    # <stddef.h>
    "size_t", "ptrdiff_t", "wchar_t", "max_align_t", "nullptr_t",  # nullptr_t is C23

    # <stdint.h>
    "int8_t", "int16_t", "int32_t", "int64_t",
    "uint8_t", "uint16_t", "uint32_t", "uint64_t",
    "int_least8_t", "int_least16_t", "int_least32_t", "int_least64_t",
    "uint_least8_t", "uint_least16_t", "uint_least32_t", "uint_least64_t",
    "int_fast8_t", "int_fast16_t", "int_fast32_t", "int_fast64_t",
    "uint_fast8_t", "uint_fast16_t", "uint_fast32_t", "uint_fast64_t",
    "intptr_t", "uintptr_t", "intmax_t", "uintmax_t",

    # <stdio.h>
    "FILE", "fpos_t",

    # <time.h>
    "time_t", "clock_t", "struct tm", "struct timespec",

    # <stdarg.h>
    "va_list",

    # <stdlib.h>
    "div_t", "ldiv_t", "lldiv_t",

    # <setjmp.h>
    "jmp_buf",

    # <signal.h>
    "sig_atomic_t",

    # <wchar.h>
    "wint_t", "mbstate_t",

    # <locale.h>
    "struct lconv",

    # <threads.h> (C11)
    "thrd_t", "mtx_t", "cnd_t", "tss_t", "once_flag", "thrd_start_t", "tss_dtor_t",

    # <stdatomic.h> (C11)
    "atomic_flag", "memory_order",
    "atomic_bool", "atomic_char", "atomic_int", "atomic_long", "atomic_llong",
    "atomic_uint", "atomic_ulong", "atomic_ullong", "atomic_size_t",
    "atomic_intptr_t", "atomic_uintptr_t", "atomic_ptrdiff_t",
    "atomic_intmax_t", "atomic_uintmax_t",

    # <uchar.h>
    "char8_t",  # C23
    "char16_t", "char32_t",
    "bool"
}

C_FUNCTIONS = {
    # <stdio.h>
    "printf", "fprintf", "sprintf", "snprintf",
    "vprintf", "vfprintf", "vsprintf", "vsnprintf",
    "scanf", "fscanf", "sscanf", "vscanf", "vfscanf", "vsscanf",
    "fopen", "freopen", "fclose", "fflush",
    "fread", "fwrite",
    "fgetc", "getc", "fgets", "fputc", "putc", "fputs",
    "getchar", "putchar", "puts", "gets_s",
    "ungetc",
    "fseek", "ftell", "rewind", "fgetpos", "fsetpos",
    "fseeko", "ftello",
    "feof", "ferror", "clearerr", "perror",
    "remove", "rename", "tmpfile", "tmpnam",
    "setbuf", "setvbuf",

    # <stdlib.h>
    "malloc", "calloc", "realloc", "free", "aligned_alloc", "free_sized", "free_aligned_sized",  # last two C23
    "atof", "atoi", "atol", "atoll",
    "strtod", "strtof", "strtold",
    "strtol", "strtoll", "strtoul", "strtoull",
    "rand", "srand",
    "abort", "exit", "_Exit", "quick_exit",
    "atexit", "at_quick_exit",
    "system", "getenv",
    "bsearch", "qsort", "qsort_r",
    "abs", "labs", "llabs",
    "div", "ldiv", "lldiv",
    "mblen", "mbtowc", "wctomb", "mbstowcs", "wcstombs",

    # <string.h>
    "memcpy", "memmove", "memcmp", "memchr", "memset",
    "memccpy",
    "strcpy", "strncpy", "strcat", "strncat", "strcmp", "strncmp",
    "strchr", "strrchr", "strstr", "strpbrk", "strspn", "strcspn",
    "strtok", "strtok_r",
    "strlen", "strerror", "strcoll", "strxfrm",
    "strdup", "strndup",
    "memset_explicit", "memset_s",  # newer / annex-K style

    # <ctype.h>
    "isalnum", "isalpha", "isblank", "iscntrl", "isdigit", "isgraph",
    "islower", "isprint", "ispunct", "isspace", "isupper", "isxdigit",
    "tolower", "toupper",

    # <math.h>
    "sin", "cos", "tan", "asin", "acos", "atan", "atan2",
    "sinh", "cosh", "tanh", "asinh", "acosh", "atanh",
    "exp", "exp2", "expm1", "log", "log2", "log10", "log1p", "logb",
    "pow", "sqrt", "cbrt", "hypot",
    "ceil", "floor", "trunc", "round", "lround", "llround", "nearbyint", "rint", "lrint", "llrint",
    "fmod", "remainder", "remquo",
    "copysign", "nan", "nextafter", "nexttoward",
    "fdim", "fmax", "fmin", "fma",
    "fabs", "frexp", "ldexp", "modf", "scalbn", "scalbln",
    "ilogb", "erf", "erfc", "tgamma", "lgamma",
    "isfinite", "isinf", "isnan", "isnormal", "signbit",
    "isgreater", "isgreaterequal", "isless", "islessequal", "islessgreater", "isunordered",

    # <time.h>
    "time", "difftime", "mktime", "asctime", "ctime",
    "gmtime", "localtime", "strftime",
    "clock", "timespec_get", "timespec_getres",  # timespec_getres is C23

    # <wchar.h>, <wctype.h> — wide-char variants
    "wcslen", "wcscpy", "wcsncpy", "wcscat", "wcsncat", "wcscmp", "wcsncmp",
    "wcschr", "wcsrchr", "wcsstr", "wcstok",
    "fwprintf", "fwscanf", "swprintf", "swscanf", "wprintf", "wscanf",
    "iswalpha", "iswdigit", "iswspace", "towlower", "towupper",

    # <setjmp.h>
    "setjmp", "longjmp",

    # <signal.h>
    "signal", "raise",

    # <assert.h>
    # assert() is a macro, listed above

    # <locale.h>
    "setlocale", "localeconv",

    # <stdarg.h> (function-like macros)
    "va_start", "va_arg", "va_end", "va_copy",

    # <threads.h>
    "thrd_create", "thrd_join", "thrd_detach", "thrd_exit", "thrd_yield",
    "thrd_sleep", "thrd_current", "thrd_equal",
    "mtx_init", "mtx_lock", "mtx_unlock", "mtx_trylock", "mtx_timedlock", "mtx_destroy",
    "cnd_init", "cnd_signal", "cnd_broadcast", "cnd_wait", "cnd_timedwait", "cnd_destroy",
    "call_once",
    "tss_create", "tss_get", "tss_set", "tss_delete",

    # <stdatomic.h>
    "atomic_init", "atomic_store", "atomic_load", "atomic_exchange",
    "atomic_compare_exchange_strong", "atomic_compare_exchange_weak",
    "atomic_fetch_add", "atomic_fetch_sub", "atomic_fetch_or",
    "atomic_fetch_and", "atomic_fetch_xor",
    "atomic_flag_test_and_set", "atomic_flag_clear",
    "atomic_thread_fence", "atomic_signal_fence", "atomic_is_lock_free",

    # <uchar.h>
    "mbrtoc8", "c8rtomb",  # C23
    "mbrtoc16", "c16rtomb", "mbrtoc32", "c32rtomb",

    # <stdbit.h> (C23) — bit utilities
    "stdc_leading_zeros", "stdc_leading_ones", "stdc_trailing_zeros", "stdc_trailing_ones",
    "stdc_first_leading_zero", "stdc_first_leading_one",
    "stdc_first_trailing_zero", "stdc_first_trailing_one",
    "stdc_count_zeros", "stdc_count_ones", "stdc_has_single_bit",
    "stdc_bit_width", "stdc_bit_floor", "stdc_bit_ceil",
}

C_KEYWORDS = {
    "auto", "break", "case", "char", "const", "continue",
    "default", "do", "else", "enum", "extern",
    "float", "for", "goto", "if", "int", "long",
    "register", "return", "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union", "unsigned", "void",
    "volatile", "while",
    "inline",
    "restrict",
    "_Bool",
    "_Complex",
    "_Imaginary",
    "_Alignas",
    "_Alignof",
    "_Atomic",
    "_Generic",
    "_Noreturn",
    "_Static_assert",
    "_Thread_local",
    "alignas",   
    "alignof",   
    "bool",          
    "true",     
    "false",     
    "static_assert",
    "thread_local",
    "typeof",
    "typeof_unqual",
    "constexpr",
    "nullptr",
    "_BitInt",
    "_Decimal32",
    "_Decimal64",
    "_Decimal128",
}

class WINDOW:
    def __init__(self):
        self.file = ""
        self.multiline_comment = False
        self.fontsize = COMMON_FONTSIZE
        self.indent_size = 4
        self.indented_count = 0
        self.window = tk.Tk()
        self.font = COMMON_FONT
        if self.font not in tkfont.families():
            self.font = "Courier New"
        x = int((self.window.winfo_screenwidth() - self.window.winfo_screenwidth() / 1.4) // 2)
        y = int((self.window.winfo_screenheight() - (self.window.winfo_screenheight() / 1.2) - 75) // 2)
        self.window.geometry(f"{int(self.window.winfo_screenwidth() / 1.4)}x{int(self.window.winfo_screenheight() / 1.2)}+{x}+{y}")
        self.window.state("zoomed")
        self.window.title("CLIDE")
        self.window.grid_rowconfigure(0, weight = 1)
        self.window.grid_rowconfigure(1, weight = 0)
        self.window.grid_columnconfigure(0, weight = 0)
        self.window.grid_columnconfigure(1, weight = 1)
        self.window.grid_columnconfigure(2, weight = 0)
        try:
            self.window.iconbitmap(LOGO_ICO)
        except:
            messagebox.showerror("Logo Error", f"Unable to find {LOGO_ICO}")
        
        self.main_menubar = tk.Menu(self.window)
        self.main_menubar_file_menu = tk.Menu(self.main_menubar, tearoff=0)
        self.main_menubar_file_menu.add_command(label="Open", command = self.open_file)
        self.main_menubar_file_menu.add_command(label="Save", command = self.save_file)
        self.main_menubar_file_menu.add_command(label="Save as", command = self.saveas_file)
        self.main_menubar_file_menu.add_separator()
        self.main_menubar_file_menu.add_command(label="Exit", command=self.window.quit)
        
        self.main_menubar_run_menu = tk.Menu(self.main_menubar, tearoff=0)
        self.main_menubar_run_menu.add_command(label="Run C file     F5", command = self.run_file)
        self.main_menubar.add_cascade(label="File", menu=self.main_menubar_file_menu)
        self.main_menubar.add_cascade(label="Run", menu=self.main_menubar_run_menu)
        self.window.config(menu=self.main_menubar)
        
        self.main_scrollbar_x = tk.Scrollbar(self.window, orient="horizontal")
        self.main_scrollbar_x.grid(row = 1, column = 0, columnspan = 2, sticky = "ew")
        
        self.main_scrollbar_y = tk.Scrollbar(self.window, orient="vertical")
        self.main_scrollbar_y.grid(row = 0, column = 2, sticky = "ns")
        
        self.line_numbers_width = 20
        
        self.line_numbers = tk.Canvas(self.window, highlightthickness=0,
                                      width = self.line_numbers_width, bg = COMMON_BG)
        self.line_numbers.grid(row = 0, column = 0, sticky = "ns")
        
        def on_textscroll(first, last):
            self.main_scrollbar_y.set(first, last)
            self.update_clide()
            
        self.editor = tk.Text(self.window ,
                              bg = COMMON_BG,
                              insertbackground="gray70",
                              fg = "white" ,
                              wrap="none",
                              undo=True,
                              maxundo=-1,
                              font = (self.font, COMMON_FONTSIZE, "bold"),
                              xscrollcommand = self.main_scrollbar_x.set,
                              yscrollcommand=on_textscroll)
        self.editor.grid(row = 0, column = 1, sticky = "nsew")
        self.editor.edit_modified(False)
        self.editor.tag_configure("keyword", foreground="#569CD6")
        self.editor.tag_configure("type", foreground="#4EC9B0")
        self.editor.tag_configure("string", foreground="#CE9178")
        self.editor.tag_configure("comment", foreground="#6A9955")
        self.editor.tag_configure("number", foreground="#B5CEA8")
        self.editor.tag_configure("preprocessor", foreground="#C586C0")

        self.main_scrollbar_x.config(command = self.editor.xview)
        self.main_scrollbar_y.config(command = self.editor.yview)
        self.editor.bind("<KeyRelease>", self.update_clide)
        self.editor.bind("<Control-o>", self.open_file)
        self.editor.bind("<Control-s>", self.save_file)
        self.editor.bind("<Return>", self.indent_line)
        self.editor.bind("<F5>", self.run_file)
        self.editor.bind("<Control-v>", self.paste_text)
        self.editor.bind("<Control-MouseWheel>", self.zoom_text)
        self.editor.tag_configure("keyword", foreground="yellow")
        self.editor.tag_configure("string", foreground="#ff8080")
        self.editor.tag_configure("preprocessor", foreground="orange")
        self.editor.tag_configure("brackets", foreground="lightblue")
        self.editor.tag_configure("functions", foreground="violet")
        self.editor.tag_configure("comment", foreground="grey")
        self.editor.tag_configure("type", foreground="green")

    def paste_text(self, event=None):
        start = self.editor.index("insert")

        try:
            data = self.editor.clipboard_get()
        except tk.TclError:
            return "break"
        self.editor.insert("insert", data)

        end = self.editor.index(f"{start}+{len(data)}c")
        pasted_first_line = int(self.editor.index(start).split(".")[0])
        pasted_last_line = int(self.editor.index(end).split(".")[0])

        for line in range(pasted_first_line, pasted_last_line + 1):
            self.syntax_highlight(f"{line}.0", f"{line}.end")
        
        return "break"
    
    def zoom_text(self, event=None):
        if event:
            if event.delta > 0:
                if self.fontsize >= 80:
                    return
                self.fontsize += 1
                self.editor.configure(font=(self.font, self.fontsize, "bold"))
                self.line_numbers_width += 1
                self.line_numbers.configure(width = self.line_numbers_width)
                self.update_clide()
            
            elif event.delta < 0:
                if self.fontsize <= 10:
                    return
                self.fontsize -= 1
                self.editor.configure(font=(self.font, self.fontsize, "bold"))
                self.line_numbers_width -= 1
                self.line_numbers.configure(width = self.line_numbers_width)
                self.update_clide()
    
    def indent_line(self, event=None):
        line = self.editor.get("insert linestart", "insert")

        indent = len(line) - len(line.lstrip(" "))

        if line.rstrip().endswith(("{", ":")):
            indent += self.indent_size
        elif line.rstrip().endswith("}"):
            indent -= self.indent_size
        self.editor.insert("insert", "\n" + " " * indent)
        return "break"
    
    def syntax_highlight(self, start, end):
        if self.multiline_comment:
            self.editor.tag_add( "comment", start, end)
        words = self.editor.get(start, end)
        lc = len(words)
        word = ""
        in_string = False
        in_preprocessor = False
        string_start = 0
        for i in range(0, lc, 1):
            if words[i] in (" ", "\t"):
                continue
            word += words[i]
            if words[i:i+2] == "//" and not in_string and not in_preprocessor:
                self.editor.tag_add( "comment", f"{start}+{i-1}c", end)
                break
                
            elif words[i:i+2] == "/*" and not in_string and not in_preprocessor:
                self.multiline_comment = True
                self.editor.tag_add( "comment", f"{start}+{i-1}c", end)
                continue
            
            elif words[i:i+2] == "*/" and not in_string and not in_preprocessor:
                self.multiline_comment = False
                continue
                
            elif word in C_TYPES:
                self.editor.tag_add( "type", f"{start}+{i-len(word)+1}c", f"{start}+{i+1}c")
            
            elif word in C_KEYWORDS:
                self.editor.tag_add( "keyword", f"{start}+{i-len(word)+1}c", f"{start}+{i+1}c")
                
            elif word in C_FUNCTIONS:
                self.editor.tag_add( "functions", f"{start}+{i-len(word)+1}c", f"{start}+{i+1}c")
                word = ""
                
            elif words[i] == '"':
                if not in_string:
                    in_string = True
                    string_start = i
                else:
                    in_string = False
                    self.editor.tag_add( "string", f"{start}+{string_start}c", f"{start}+{i+1}c")
                
            elif words[i] in "{}()[];,+-*=<>":
                self.editor.tag_add( "brackets", f"{start}+{i}c", f"{start}+{i+1}c")
                word = ""
            
            elif words[i:i+1] == "#":
                self.editor.tag_add( "preprocessor", f"{start}+{i}c", end)
                break
            
    def update_clide(self, event=None):
        start = self.editor.index("insert linestart")
        end = self.editor.index("insert lineend")
        self.syntax_highlight(start, end)
        if self.editor.edit_modified() and self.file:
            self.window.title(f"CLIDE - *{self.file}")
            
        self.line_numbers.delete("all")
        line_count = int(self.editor.index("end-1c").split(".")[0])
        digits = len(str(line_count))
        self.line_numbers.config(width=digits * self.fontsize + 1)
        index = self.editor.index("@0,0")

        while True:
            info = self.editor.dlineinfo(index)
            if info is None:
                break

            y = info[1]
            line = index.split(".")[0]

            self.line_numbers.create_text(5, y, font = (self.font, self.fontsize), fill="gray50", text=line, anchor="nw")
            index = self.editor.index(f"{index}+1line")
    
    def run_file(self, event=None):
        if not self.file:
            messagebox.showerror("No File", "Currently No File is opened")
            return
        exe = os.path.splitext(self.file)[0] + ".exe"

        subprocess.Popen(f'cmd /k gcc "{self.file}" -o "{exe}" && "{exe}" & pause & exit', creationflags=subprocess.CREATE_NEW_CONSOLE)
    
    def open_file(self, event=None):
        filename = filedialog.askopenfilename(
            filetypes=[
                ("All Files", "*.*")
            ]
        )
        if not filename:
            return
        
        size = os.path.getsize(filename)
        size = size / 1024**2
        if (size) > 1:
            permission = messagebox.askyesno("Warning", f"Loading This File Could Take Time\n Size of the file is {size} mb\n Do you want to load it ?")
            if not permission:
                return
        text = None
        try:
            with open(filename, "r", encoding="utf-8") as f:
                text = f.read().expandtabs(4)
        except Exception as e:
            messagebox.showerror("Unable", f"Unable to Load File {e}")
        
        self.editor.delete("1.0", "end")
        self.editor.insert("1.0", text)
        self.multiline_comment = False
        last_line = int(self.editor.index("end-1c").split(".")[0])

        for line in range(1, last_line + 1):
            self.syntax_highlight(f"{line}.0", f"{line}.end")

        self.file = filename
        self.editor.edit_modified(False)
        self.window.title(f"CLIDE - {self.file}")
        self.update_clide()
    
    def save_file(self, event=None):
        if not self.file:
            return
            
        with open(self.file, "w", encoding="utf-8") as f:
            f.write(self.editor.get("1.0", "end-1c"))
        
        self.update_clide()
        self.editor.edit_modified(False)
        self.window.title(f"CLIDE - {self.file}")
    
    def saveas_file(self, event=None):
        path = filedialog.asksaveasfilename(
            defaultextension=".c",
            filetypes=[("C source", "*.c"), ("All Files", "*.*")]
        )
        if not path:
            return
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.editor.get("1.0", "end-1c"))
        self.file = path
        self.editor.edit_modified(False)
        self.window.title(f"CLIDE - {self.file}")
        self.update_clide()

window = WINDOW()
window.window.mainloop()