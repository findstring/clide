import tkinter as tk
import os, sys, subprocess
import tkinter.font as tkfont
from tkinter import colorchooser, ttk, simpledialog, filedialog, messagebox

CLIDE_VERSION = "v0.2.2"
SCRIPT_PATH = os.path.abspath(__file__)
LOGO_ICO = os.path.join(os.path.dirname(SCRIPT_PATH), "icons", "logo.ico")
LOGO_PNG = os.path.join(os.path.dirname(SCRIPT_PATH), "icons", "logo.png")
COMMON_BG = "gray5"
COMMON_FG = "gray70"
COMMON_FONTSIZE = 16
COMMON_FONT = "Iosevka"

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
        self.button_frame_list = []
        self.is_saved = True
        self.upper_frame = None
        self.files_opened = {}
        self.file = None
        self.multiline_comment = False
        self.fontsize = COMMON_FONTSIZE
        self.bgcolor = COMMON_BG
        self.fgcolor = COMMON_FG
        self.indent_size = 4
        self.indented_count = 0
        self.window = tk.Tk()
        self.window.configure(bg = "#0a0a0a")
        self.main_frame = None
        self.editor = None
        self.line_numbers = None
        self.main_scrollbar_x = None
        self.main_scrollbar_y = None
        self.line_numbers_width = 20
        self.font = COMMON_FONT
        if self.font not in tkfont.families():
            self.font = "Courier New"
        x = int((self.window.winfo_screenwidth() - self.window.winfo_screenwidth() / 1.4) // 2)
        y = int((self.window.winfo_screenheight() - (self.window.winfo_screenheight() / 1.2) - 75) // 2)
        self.window.geometry(f"{int(self.window.winfo_screenwidth() / 1.4)}x{int(self.window.winfo_screenheight() / 1.2)}+{x}+{y}")
        self.window.state("zoomed")
        self.window.title("CLIDE")
        self.window.grid_rowconfigure(0, weight = 0)
        self.window.grid_rowconfigure(1, weight = 1)
        self.window.grid_columnconfigure(0, weight = 1)
        try:
            self.window.iconbitmap(LOGO_ICO)
        except:
            messagebox.showerror("Logo Error", f"Unable to find {LOGO_ICO}")
        
        self.main_menubar = tk.Menu(self.window)
        self.main_menubar_file_menu = tk.Menu(self.main_menubar, tearoff=0)
        self.main_menubar_file_menu.add_command(label="New", command = self.new_file)
        self.main_menubar_file_menu.add_command(label="Open", command = self.open_file)
        self.main_menubar_file_menu.add_command(label="Save", command = self.save_file)
        self.main_menubar_file_menu.add_separator()
        self.main_menubar_file_menu.add_command(label="Exit", command=self.exit_app)
        self.main_menubar.add_cascade(label="File", menu=self.main_menubar_file_menu)
        
        self.main_menubar_run_menu = tk.Menu(self.main_menubar, tearoff=0)
        self.main_menubar_run_menu.add_command(label="Run C file     F5", command = self.run_file)
        self.main_menubar.add_cascade(label="Run", menu=self.main_menubar_run_menu)
        
        self.main_menubar_settings_menu = tk.Menu(self.main_menubar, tearoff=0)
        self.main_menubar_settings_menu.add_command(label="Style Configurator...", command = self.style_configurator)
        self.main_menubar_settings_menu.add_command(label="About and Info...", command = self.about_info)
        self.main_menubar.add_cascade(label="Settings", menu=self.main_menubar_settings_menu)
        self.window.config(menu=self.main_menubar)
        self.window.protocol("WM_DELETE_WINDOW", self.exit_app)
        
        self.logo_png = tk.PhotoImage(file=LOGO_PNG)
        self.logo_label = tk.Label(self.window, image=self.logo_png)
        self.logo_label.grid(row = 0, column = 0, sticky = "w", pady = (30,0), padx = 30)
        self.new_file_button = tk.Button(self.window, text = "📝 New File", command = self.new_file, bg = "#0a0a0a", relief = "flat", font = ("Consolas", 50), fg = "white")
        self.new_file_button.grid(row = 0, column = 1, pady = (0, 500), padx =(0, 150))
        self.open_file_button = tk.Button(self.window, text = "📂 Open File", command = self.open_file, bg = "#0a0a0a", relief = "flat", font = ("Consolas", 50), fg = "white")
        self.open_file_button.grid(row = 0, column = 1, pady = (0, 0), padx =(0, 150))
        self.exit_file_button = tk.Button(self.window, text = "🚪  Exit App", bg = "#0a0a0a", command = self.exit_app, relief = "flat", font = ("Consolas", 50), fg = "white")
        self.exit_file_button.grid(row = 0, column = 1, pady = (500, 0), padx =(0, 150))
    
    def exit_app(self):
        if self.is_saved == False:
            saved = messagebox.askyesno("Save before exit", "Do you want to save the current file before exit ?")
            if not saved:
                self.window.destroy()
                return
        
        self.save_file()
        self.window.destroy()
            
    def create_tab_area(self):
        self.upper_frame = tk.Frame(self.window, bg = COMMON_BG, height = 45)
        self.upper_frame.grid(row = 0, column = 0, columnspan = 3, sticky = "ew")
        
        self.upper_frame.grid_rowconfigure(0, weight = 1)
        self.upper_frame.grid_rowconfigure(1, weight = 0)
        
        self.upper_frame.grid_columnconfigure(0, weight = 1)
        
        self.tab_scrollbar = tk.Scrollbar(
            self.upper_frame,
            orient="horizontal"
        )

        self.tab_canvas = tk.Canvas(
            self.upper_frame,
            height=45,
            xscrollcommand=self.tab_scrollbar.set,
            bg=COMMON_BG,
            relief="sunken"
        )

        self.tab_scrollbar.config(command=self.tab_canvas.xview)

        self.tab_canvas.grid(row=0, column=0, sticky="ew")
        self.tab_scrollbar.grid(row=1, column=0, sticky="ew")

        self.canvas_inside_frame = tk.Frame(self.tab_canvas)

        self.tab_canvas.create_window(
            (0, 0),
            window=self.canvas_inside_frame,
            anchor="nw"
        )
        
        def update_canvas_scrollregion(event=None):
            self.tab_canvas.configure(
                scrollregion=self.tab_canvas.bbox("all")
            )

        self.canvas_inside_frame.bind(
            "<Configure>",
            update_canvas_scrollregion
        )
    
    def hide_file(self, filename):
        self.files_opened[filename][0].grid_remove()
    
    def add_file(self, filename):
        if self.logo_label:
            self.logo_label.destroy()
            self.logo_label = None
        
        if self.new_file_button:
            self.new_file_button.destroy()
            self.new_file_button = None
        
        if self.open_file_button:
            self.open_file_button.destroy()
            self.open_file_button = None
            
        if self.exit_file_button:
            self.exit_file_button.destroy()
            self.exit_file_button = None
            
        if not self.upper_frame:
            self.create_tab_area()
        frame = tk.Frame(self.window, bg = COMMON_BG)
        frame.grid(row = 1, column = 0, sticky = "nsew")
        
        frame.grid_rowconfigure(0, weight = 1)
        frame.grid_rowconfigure(1, weight = 0)
        
        frame.grid_columnconfigure(0, weight = 0)
        frame.grid_columnconfigure(1, weight = 1)
        frame.grid_columnconfigure(2, weight = 0)
        
        main_scrollbar_x = tk.Scrollbar(frame, orient="horizontal")
        main_scrollbar_x.grid(row = 1, column = 0, columnspan = 3, sticky = "ew")
        
        main_scrollbar_y = tk.Scrollbar(frame, orient="vertical")
        main_scrollbar_y.grid(row = 0, column = 2, sticky = "ns")
        
        line_numbers = tk.Canvas(frame, highlightthickness=0, width = self.line_numbers_width, bg = self.bgcolor)
        line_numbers.grid(row = 0, column = 0, sticky = "ns")
        
        def on_textscroll(first, last):
            main_scrollbar_y.set(first, last)
            self.update_clide()
            
        editor = tk.Text(frame ,
                              bg = self.bgcolor,
                              insertbackground="gray70",
                              fg = self.fgcolor ,
                              wrap="none",
                              undo=True,
                              maxundo=-1,
                              font = (self.font, COMMON_FONTSIZE),
                              xscrollcommand = main_scrollbar_x.set,
                              yscrollcommand=on_textscroll)
        editor.grid(row = 0, column = 1, sticky = "nsew")
        editor.edit_modified(False)

        main_scrollbar_x.config(command = editor.xview)
        main_scrollbar_y.config(command = editor.yview)
        editor.bind("<KeyRelease>", self.update_clide)
        editor.bind("<Control-o>", self.open_file)
        editor.bind("<Control-s>", self.save_file)
        editor.bind("<Return>", self.indent_line)
        editor.bind("<F5>", self.run_file)
        editor.bind("<Control-v>", self.paste_text)
        editor.bind("<Control-MouseWheel>", self.zoom_text)
        editor.tag_configure("keyword", foreground="yellow")
        editor.tag_configure("string", foreground="#ff8080")
        editor.tag_configure("preprocessor", foreground="orange")
        editor.tag_configure("brackets", foreground="lightblue")
        editor.tag_configure("functions", foreground="violet")
        editor.tag_configure("comment", foreground="grey")
        editor.tag_configure("type", foreground="green")
        
        self.files_opened[filename] = [frame, editor, line_numbers, main_scrollbar_x, main_scrollbar_y]
        self.main_frame = frame
        self.editor = editor
        self.line_numbers = line_numbers
        self.main_scrollbar_x = main_scrollbar_x
        self.main_scrollbar_y = main_scrollbar_y
        
        def shorten(filename):
            if len(filename) > 20:
                name = filename[:20] + "..."
                return name
            else:
                return filename
        
        button_frame = tk.Frame(
            self.canvas_inside_frame,
            width=80,
            height=45,
            relief="flat"
        )

        button_frame.pack(side="left", padx = 1, pady = 2)
        button_frame.grid_columnconfigure(0, weight = 1)
        button_frame.grid_columnconfigure(1, weight = 0)
        
        basename = os.path.basename(filename)
        
        tk.Button(button_frame,
                  bg = COMMON_BG,
                  fg = COMMON_FG,
                  text = shorten(basename),
                  font = (COMMON_FONT, 15),
                  command = lambda : self.select_file(filename)
        ).grid(row = 0, column = 0, sticky = "nsew")
        
        def button_command(filename):
            self.remove_file(filename)
            button_frame.destroy()
            
        tk.Button(button_frame, bg = COMMON_BG, fg = COMMON_FG, text = "❌", relief = "flat", command = lambda : button_command(filename)).grid(row = 0, column = 1, sticky = "nsew")
        self.button_frame_list.append(button_frame)
    
    def remove_file(self, filename):
        if filename not in self.files_opened:
            return
        
        if self.is_saved == False:
            saved = messagebox.askyesno("Save before exit", "Do you want to save the current file before exit ?")
            if not saved:
                pass
            else:
                self.save_file()
            
        self.files_opened[filename][0].destroy()
        self.main_frame = None
        self.editor = None
        self.line_numbers = None
        self.main_scrollbar_x = None
        self.main_scrollbar_y = None
        del self.files_opened[filename]
        if len(self.files_opened) > 0:
            self.select_file(list(self.files_opened.keys())[0])
            return
        
        elif len(self.files_opened) == 0:
            self.upper_frame.destroy()
            self.upper_frame = None
            self.main_frame = None
            self.editor = None
            self.line_numbers = None
            self.main_scrollbar_x = None
            self.main_scrollbar_y = None
            self.file = None
            self.logo_label = tk.Label(self.window, image=self.logo_png)
            self.logo_label.grid(row = 0, column = 0, sticky = "w", pady = (30,0), padx = 30)
            self.new_file_button = tk.Button(self.window, text = "📝 New File", command = self.new_file, bg = "#0a0a0a", relief = "flat", font = ("Consolas", 50), fg = "white")
            self.new_file_button.grid(row = 0, column = 1, pady = (0, 500), padx =(0, 150))
            self.open_file_button = tk.Button(self.window, text = "📂 Open File", command = self.open_file, bg = "#0a0a0a", relief = "flat", font = ("Consolas", 50), fg = "white")
            self.open_file_button.grid(row = 0, column = 1, pady = (0, 0), padx =(0, 150))
            self.exit_file_button = tk.Button(self.window, text = "🚪  Exit App", bg = "#0a0a0a", command = self.exit_app, relief = "flat", font = ("Consolas", 50), fg = "white")
            self.exit_file_button.grid(row = 0, column = 1, pady = (500, 0), padx =(0, 150))
    
    def run_file(self, event=None):
        if not self.file:
            messagebox.showerror("No File", "Currently No File is opened")
            return
        exe = os.path.splitext(self.file)[0] + ".exe"

        subprocess.Popen(f'cmd /k gcc "{self.file}" -o "{exe}" && "{exe}" & pause & exit', creationflags=subprocess.CREATE_NEW_CONSOLE)
    
    def select_file(self, filename):
        if filename == None:
            return
            
        if self.main_frame and self.main_frame.winfo_ismapped():
            self.main_frame.grid_remove()
        self.main_frame, self.editor, self.line_numbers, self.main_scrollbar_x, self.main_scrollbar_y = self.files_opened[filename]
        self.main_frame.grid()
        self.file = filename
        self.window.title(f"CLIDE - {self.file}")
    
    def new_file(self, event=None):
        filename = simpledialog.askstring("Filename", "Enter Filename")
        if not filename:
            return
        
        directory = filedialog.askdirectory()
        if not directory:
            return
        
        filepath = os.path.join(directory, filename)
        
        open(filepath, "w").close()
        
        if os.path.exists(filepath):
            self.file_open_helper(filepath)
    
    def open_file(self, event=None):
        filename = filedialog.askopenfilename(
            filetypes=[
                ("C Files", "*.c *.h")
            ]
        )
        if not filename:
            return
        
        self.file_open_helper(filename)
    
    def file_open_helper(self, filename):
        if filename in self.files_opened and filename != self.file:
            self.select_file(filename)
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
            return
        
        if self.file:
            self.hide_file(self.file)
        self.add_file(filename)
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
        self.is_saved = True
    
    def style_configurator(self, event = None):
        win = tk.Toplevel(self.window)
        win.attributes("-topmost", True)
        win.title("Style Configurator")
        x = int((win.winfo_screenwidth() - win.winfo_screenwidth() / 3) // 2)
        y = int((win.winfo_screenheight() - (win.winfo_screenheight() / 2.5) - 75) // 2)
        win.geometry(f"{int(win.winfo_screenwidth() / 3)}x{int(win.winfo_screenheight() / 2.5)}+{x}+{y}")
        try:
            win.iconbitmap(LOGO_ICO)
        except:
            messagebox.showerror("Logo Error", f"Unable to find {LOGO_ICO}")
        win.focus_force()
        win.focus_set()
        win.configure(bg=self.bgcolor)
        win.grid_rowconfigure(0, weight = 1)
        win.grid_rowconfigure(1, weight = 1)
        win.grid_rowconfigure(2, weight = 1)
        win.grid_columnconfigure(0, weight = 1)
        win.grid_columnconfigure(1, weight = 1)
        
        def change_fg():
            fg = colorchooser.askcolor()
            if not fg[1]:
                return
            fg = fg[1]
            self.fgcolor = fg
            self.editor.configure(fg = self.fgcolor)
            fg_button.config(text=f"{self.fgcolor} ➕", fg=self.fgcolor)
            self.update_clide()
        
        def change_bg():
            bg = colorchooser.askcolor()
            if not bg[1]:
                return
            bg = bg[1]
            self.bgcolor = bg
            self.editor.configure(bg = self.bgcolor)
            bg_button.config(text=f"{self.bgcolor} ➕", fg=self.bgcolor)
            self.line_numbers.configure(bg = self.bgcolor)
            self.update_clide()
        
        tk.Label(win, text = "Foreground Colour ", font = (self.font, 14), bg = self.bgcolor ,fg = "gray70").grid(row = 0, column = 0, padx = 30, sticky = "w")
        fg_button = tk.Button(win, relief = "flat",font = (self.font, 14), text = f"{self.fgcolor} ➕", bg ="gray30" ,fg = self.fgcolor, command = change_fg)
        fg_button.grid(row = 0, column = 1, sticky = "w", columnspan = 1)
        
        tk.Label(win, text = "Background Colour ",font = (self.font, 14), bg = self.bgcolor ,fg = "gray70").grid(row = 1, column = 0, padx = 30, sticky = "w")
        bg_button = tk.Button(win, relief = "flat",font = (self.font, 14), text = f"{self.bgcolor} ➕", bg ="gray30" ,fg = self.fgcolor, command = change_bg)
        bg_button.grid(row = 1, column = 1, sticky = "w", columnspan = 1)
        
        tk.Label(
            win,
            text="Font",
            font=(self.font, 14),
            bg=self.bgcolor,
            fg="gray70"
        ).grid(row=2, column=0, padx = 30, sticky="w")
        
        choice = tk.StringVar(value=self.font)
        
        def change_font(event = None):
            self.font = combo.get()
            self.editor.configure(font = (self.font, self.fontsize))
            self.update_clide()
        
        fonts = sorted(tkfont.families())
        combo = ttk.Combobox(
            win,
            textvariable=choice,
            values=fonts,
            state="readonly",
            width=30,
        )
        combo.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        win.after(100, lambda: combo.set(self.font))
        combo.bind("<<ComboboxSelected>>", change_font)
    
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
                self.editor.configure(font=(self.font, self.fontsize))
                self.line_numbers_width += 1
                self.line_numbers.configure(width = self.line_numbers_width)
                self.update_clide()
            
            elif event.delta < 0:
                if self.fontsize <= 10:
                    return
                self.fontsize -= 1
                self.editor.configure(font=(self.font, self.fontsize))
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
        self.editor.tag_remove("keyword", start, end)
        self.editor.tag_remove("type", start, end)
        self.editor.tag_remove("functions", start, end)
        self.editor.tag_remove("string", start, end)
        self.editor.tag_remove("comment", start, "end")
        self.editor.tag_remove("preprocessor", start, end)
        self.editor.tag_remove("brackets", start, end)

        words = self.editor.get(start, end)
        lc = len(words)
        
        if self.multiline_comment and words.find("*/") == -1 and words.find("/*") == -1:
            self.editor.tag_add("comment", start, end)
            return

        word = ""
        word_start = 0

        in_string = False
        in_char = False
        in_preprocessor = False

        string_start = 0
        char_start = 0

        IDENT = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        i = 0
        while i < lc:

            ch = words[i]

            if not in_string and not in_char and words[i:i+2] == "//":
                self.editor.tag_add("comment", f"{start}+{i}c", end)
                break

            elif not in_string and not in_char and words[i:i+2] == "/*":
                close = words.find("*/", i + 2)
                if close == -1:
                    self.multiline_comment = True
                    self.editor.tag_add("comment", f"{start}+{i}c", end)
                    break
                else:
                    self.editor.tag_add("comment", f"{start}+{i}c", f"{start}+{close+2}c")
                    i = close + 2
                    word = ""
                    continue

            elif self.multiline_comment and words[i:i+2] == "*/":
                self.multiline_comment = False
                self.editor.tag_add("comment", start, f"{start}+{i+2}c")
                i += 2
                continue

            if ch == '"':

                if not in_string:
                    in_string = True
                    string_start = i
                else:
                    in_string = False
                    self.editor.tag_add(
                        "string",
                        f"{start}+{string_start}c",
                        f"{start}+{i+1}c"
                    )

                i += 1
                continue

            if ch == "'":

                if not in_char:
                    in_char = True
                    char_start = i
                else:
                    in_char = False
                    self.editor.tag_add(
                        "string",
                        f"{start}+{char_start}c",
                        f"{start}+{i+1}c"
                    )

                i += 1
                continue

            if in_string or in_char:
                i += 1
                continue

            if ch == "#":
                self.editor.tag_add("preprocessor", f"{start}+{i}c", end)
                break

            if ch.isalnum() or ch == "_":

                if not word:
                    word_start = i

                word += ch

                next_char = words[i + 1] if i + 1 < lc else " "

                if next_char not in IDENT:

                    if word in C_TYPES:
                        self.editor.tag_add(
                            "type",
                            f"{start}+{word_start}c",
                            f"{start}+{i+1}c"
                        )

                    elif word in C_KEYWORDS:
                        self.editor.tag_add(
                            "keyword",
                            f"{start}+{word_start}c",
                            f"{start}+{i+1}c"
                        )

                    elif word in C_FUNCTIONS:
                        self.editor.tag_add(
                            "functions",
                            f"{start}+{word_start}c",
                            f"{start}+{i+1}c"
                        )

                    word = ""

            else:
                word = ""

                if ch in "{}()[]":
                    self.editor.tag_add(
                        "brackets",
                        f"{start}+{i}c",
                        f"{start}+{i+1}c"
                    )

            i += 1
            
    def update_clide(self, event=None):
        start = self.editor.index("insert linestart")
        end = self.editor.index("insert lineend")
        self.syntax_highlight(start, end)
        if self.editor.edit_modified() and self.file:
            self.window.title(f"CLIDE - *{self.file}")
            self.is_saved = False
            
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

            self.line_numbers.create_text(5, y, font = (self.font, self.fontsize), fill=self.fgcolor, text=line, anchor="nw")
            index = self.editor.index(f"{index}+1line")
            
    def about_info(self, event = None):
        win = tk.Toplevel(self.window)
        win.attributes("-topmost", True)
        win.title("About and Info")
        try:
            win.iconbitmap(LOGO_ICO)
        except:
            messagebox.showerror("Logo Error", f"Unable to find {LOGO_ICO}")
        win.focus_force()
        win.focus_set()
        win.configure(bg=self.bgcolor)
        tk.Label(win, text ="Software name    : CLIDE", font = (self.font, 16), fg = self.fgcolor, bg = self.bgcolor).pack(pady=10, anchor = "nw")
        tk.Label(win, text =f"Software version : {CLIDE_VERSION}", font = (self.font, 16), fg = self.fgcolor, bg = self.bgcolor).pack(pady=10, anchor = "nw")
        tk.Label(win, text ="Maintainer       : Moinak debnath", font = (self.font, 16), fg = self.fgcolor, bg = self.bgcolor).pack(pady=10, anchor = "nw")
        tk.Label(win, text ="Contributors     : Claude (AI assistance)", font = (self.font, 16), fg = self.fgcolor, bg = self.bgcolor).pack(pady=10, anchor = "nw")
        tk.Label(win, text ="Description      : A code editor for C", font = (self.font, 16), fg = self.fgcolor, bg = self.bgcolor).pack(pady=10, anchor = "nw")
        tk.Label(win, text ="License          : MIT", font = (self.font, 16), fg = self.fgcolor, bg = self.bgcolor).pack(pady=10, anchor = "nw")
                
        win.update_idletasks()

        w = win.winfo_width()
        h = win.winfo_height()

        x = (win.winfo_screenwidth() - w) // 2
        y = ((win.winfo_screenheight() - h) // 2) - 50

        win.geometry(f"{w}x{h}+{x}+{y}")
    
def main():
    window = WINDOW()
    window.window.mainloop()


if __name__ == "__main__":
    main()