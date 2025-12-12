import tkinter as tk
from tkinter import ttk, messagebox

class PaperPriceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("书法纸价格换算")
        self.root.geometry("700x730")
        self.root.resizable(False, False)
        
        # 设置样式
        self.setup_styles()
        
        # 创建主框架
        self.create_widgets()
        
    def setup_styles(self):
        """设置控件样式"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # 配置标签样式
        style.configure('Title.TLabel', font=('Microsoft YaHei', 14, 'bold'))
        style.configure('Header.TLabel', font=('Microsoft YaHei', 12, 'bold'))
        style.configure('Normal.TLabel', font=('Microsoft YaHei', 10))
        
        # 配置按钮样式
        style.configure('Calc.TButton', font=('Microsoft YaHei', 10), padding=5)
        style.configure('AboutExit.TButton', font=('Microsoft YaHei', 10), padding=8)
        
        # 配置输入框样式
        style.configure('Input.TEntry', padding=5)
        
    def create_widgets(self):
        """创建界面组件"""
        # 主框架
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 标题
        title_label = ttk.Label(
            main_frame, 
            text="书法纸价格换算器", 
            style='Title.TLabel'
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # 第一行：参照信息
        self.create_reference_section(main_frame, 1)
        
        # 第二行：第一种计算方法
        self.create_calc1_section(main_frame, 2)
        
        # 第三行：第二种计算方法
        self.create_calc2_section(main_frame, 3)
        
        # 第四行：说明信息
        self.create_explanation_section(main_frame, 4)
        
        # 第五行：关于和退出按钮
        self.create_button_section(main_frame, 5)
        
        # 配置权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        
    def create_reference_section(self, parent, row):
        """创建参照信息部分"""
        ref_frame = ttk.LabelFrame(parent, text="参照信息", padding=10)
        ref_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        
        ref_text = """以4尺（69*138cm）100张价格作为参照：
1. 桃记宣纸棉料四尺单宣（70CM*138CM 100张/刀）1050元
2. 闲星阁一号玉扣纸（60CM*140CM 100张/刀）230元"""
        
        ref_label = ttk.Label(ref_frame, text=ref_text, style='Normal.TLabel', justify=tk.LEFT)
        ref_label.grid(row=0, column=0, sticky=tk.W)
        
    def create_calc1_section(self, parent, row):
        """创建第一种计算方法部分"""
        calc1_frame = ttk.LabelFrame(parent, text="第一种计算方法", padding=10)
        calc1_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # 输入部分
        input_frame = ttk.Frame(calc1_frame)
        input_frame.grid(row=0, column=0, columnspan=2, sticky=tk.W)
        
        # 4尺多少开
        ttk.Label(input_frame, text="4尺", style='Normal.TLabel').grid(row=0, column=0, padx=(0, 5))
        self.calc1_a = tk.StringVar()
        self.entry_calc1_a = ttk.Entry(input_frame, textvariable=self.calc1_a, width=8, style='Input.TEntry')
        self.entry_calc1_a.grid(row=0, column=1, padx=(0, 10))
        
        ttk.Label(input_frame, text="开", style='Normal.TLabel').grid(row=0, column=2, padx=(0, 5))
        self.calc1_b = tk.StringVar()
        self.entry_calc1_b = ttk.Entry(input_frame, textvariable=self.calc1_b, width=8, style='Input.TEntry')
        self.entry_calc1_b.grid(row=0, column=3, padx=(0, 10))
        
        ttk.Label(input_frame, text="张", style='Normal.TLabel').grid(row=0, column=4, padx=(0, 5))
        self.calc1_c = tk.StringVar()
        self.entry_calc1_c = ttk.Entry(input_frame, textvariable=self.calc1_c, width=8, style='Input.TEntry')
        self.entry_calc1_c.grid(row=0, column=5, padx=(0, 10))
        
        ttk.Label(input_frame, text="元", style='Normal.TLabel').grid(row=0, column=6, padx=(0, 10))
        
        # 公式显示
        formula_label = ttk.Label(
            calc1_frame, 
            text="计算公式：相对价格 = 开数 × 价格 × 100 ÷ 张数", 
            style='Normal.TLabel'
        )
        formula_label.grid(row=1, column=0, sticky=tk.W, pady=(10, 0))
        
        # 计算按钮
        calc_button = ttk.Button(
            calc1_frame, 
            text="计算", 
            command=self.calculate_method1,
            style='Calc.TButton'
        )
        calc_button.grid(row=2, column=0, sticky=tk.W, pady=(10, 0))
        
        # 结果标签
        self.calc1_result = tk.StringVar(value="结果：")
        result_label = ttk.Label(
            calc1_frame, 
            textvariable=self.calc1_result,
            style='Header.TLabel',
            foreground='blue'
        )
        result_label.grid(row=2, column=1, sticky=tk.W, pady=(10, 0), padx=(20, 0))
        
    def create_calc2_section(self, parent, row):
        """创建第二种计算方法部分"""
        calc2_frame = ttk.LabelFrame(parent, text="第二种计算方法", padding=10)
        calc2_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # 输入部分
        input_frame = ttk.Frame(calc2_frame)
        input_frame.grid(row=0, column=0, columnspan=2, sticky=tk.W)
        
        # 高多少厘米
        ttk.Label(input_frame, text="高", style='Normal.TLabel').grid(row=0, column=0, padx=(0, 5))
        self.calc2_a = tk.StringVar()
        self.entry_calc2_a = ttk.Entry(input_frame, textvariable=self.calc2_a, width=8, style='Input.TEntry')
        self.entry_calc2_a.grid(row=0, column=1, padx=(0, 10))
        ttk.Label(input_frame, text="厘米", style='Normal.TLabel').grid(row=0, column=2, padx=(0, 10))
        
        # 长多少厘米
        ttk.Label(input_frame, text="长", style='Normal.TLabel').grid(row=0, column=3, padx=(0, 5))
        self.calc2_b = tk.StringVar()
        self.entry_calc2_b = ttk.Entry(input_frame, textvariable=self.calc2_b, width=8, style='Input.TEntry')
        self.entry_calc2_b.grid(row=0, column=4, padx=(0, 10))
        ttk.Label(input_frame, text="厘米", style='Normal.TLabel').grid(row=0, column=5, padx=(0, 10))
        
        # 多少张
        ttk.Label(input_frame, text="多少", style='Normal.TLabel').grid(row=1, column=0, padx=(0, 5), pady=(10, 0))
        self.calc2_c = tk.StringVar()
        self.entry_calc2_c = ttk.Entry(input_frame, textvariable=self.calc2_c, width=8, style='Input.TEntry')
        self.entry_calc2_c.grid(row=1, column=1, padx=(0, 10), pady=(10, 0))
        ttk.Label(input_frame, text="张", style='Normal.TLabel').grid(row=1, column=2, padx=(0, 10), pady=(10, 0))
        
        # 多少钱
        ttk.Label(input_frame, text="多少", style='Normal.TLabel').grid(row=1, column=3, padx=(0, 5), pady=(10, 0))
        self.calc2_d = tk.StringVar()
        self.entry_calc2_d = ttk.Entry(input_frame, textvariable=self.calc2_d, width=8, style='Input.TEntry')
        self.entry_calc2_d.grid(row=1, column=4, padx=(0, 10), pady=(10, 0))
        ttk.Label(input_frame, text="元", style='Normal.TLabel').grid(row=1, column=5, padx=(0, 10), pady=(10, 0))
        
        # 公式显示
        formula_label = ttk.Label(
            calc2_frame, 
            text="计算公式：相对价格 = (69 × 138) ÷ (高 × 长) × (价格 ÷ 张数) × 100", 
            style='Normal.TLabel'
        )
        formula_label.grid(row=2, column=0, sticky=tk.W, pady=(10, 0))
        
        # 计算按钮
        calc_button = ttk.Button(
            calc2_frame, 
            text="计算", 
            command=self.calculate_method2,
            style='Calc.TButton'
        )
        calc_button.grid(row=3, column=0, sticky=tk.W, pady=(10, 0))
        
        # 结果标签
        self.calc2_result = tk.StringVar(value="结果：")
        result_label = ttk.Label(
            calc2_frame, 
            textvariable=self.calc2_result,
            style='Header.TLabel',
            foreground='blue'
        )
        result_label.grid(row=3, column=1, sticky=tk.W, pady=(10, 0), padx=(20, 0))
        
    def create_explanation_section(self, parent, row):
        """创建说明信息部分"""
        explanation_frame = ttk.Frame(parent)
        explanation_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
        explanation_text = """使用说明：
1. 第一种方法：用于计算不同开数的纸张相对于4尺整张纸的价格
2. 第二种方法：用于计算任意尺寸的纸张相对于4尺(69×138cm)标准纸的价格"""
        
        explanation_label = ttk.Label(
            explanation_frame, 
            text=explanation_text,
            style='Normal.TLabel',
            justify=tk.LEFT,
            foreground='gray'
        )
        explanation_label.grid(row=0, column=0, sticky=tk.W)
        
    def create_button_section(self, parent, row):
        """创建按钮部分"""
        button_frame = ttk.Frame(parent)
        button_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(20, 0))
        
        # 关于按钮
        about_button = ttk.Button(
            button_frame,
            text="关于",
            command=self.show_about,
            style='AboutExit.TButton',
            width=10
        )
        about_button.grid(row=0, column=0, padx=(0, 10))
        
        # 退出按钮
        exit_button = ttk.Button(
            button_frame,
            text="退出",
            command=self.exit_app,
            style='AboutExit.TButton',
            width=10
        )
        exit_button.grid(row=0, column=1)
        
        # 居中显示按钮
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        
    def calculate_method1(self):
        """计算方法1：a*c*100/b"""
        try:
            # 获取输入值
            a_str = self.calc1_a.get().strip()
            b_str = self.calc1_b.get().strip()
            c_str = self.calc1_c.get().strip()
            
            # 检查是否为空
            if not a_str:
                messagebox.showerror("错误", "请输入4尺的数值")
                self.entry_calc1_a.focus_set()
                return
            if not b_str:
                messagebox.showerror("错误", "请输入开数")
                self.entry_calc1_b.focus_set()
                return
            if not c_str:
                messagebox.showerror("错误", "请输入张数价格")
                self.entry_calc1_c.focus_set()
                return
                
            # 转换为浮点数
            a = float(a_str)
            b = float(b_str)
            c = float(c_str)
            
            # 检查除数是否为零
            if b == 0:
                messagebox.showerror("错误", "开数不能为0")
                self.entry_calc1_b.focus_set()
                return
                
            # 计算结果
            result = a * c * 100 / b
            self.calc1_result.set(f"结果：{result:.2f} 元/刀")
            
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字")
            # 聚焦到有问题的输入框
            if not a_str.replace('.', '', 1).isdigit() and a_str:
                self.entry_calc1_a.focus_set()
            elif not b_str.replace('.', '', 1).isdigit() and b_str:
                self.entry_calc1_b.focus_set()
            elif not c_str.replace('.', '', 1).isdigit() and c_str:
                self.entry_calc1_c.focus_set()
            
    def calculate_method2(self):
        """计算方法2：(69*138)/(a*b)*(d/c)*100"""
        try:
            # 获取输入值
            a_str = self.calc2_a.get().strip()
            b_str = self.calc2_b.get().strip()
            c_str = self.calc2_c.get().strip()
            d_str = self.calc2_d.get().strip()
            
            # 检查是否为空
            if not a_str:
                messagebox.showerror("错误", "请输入纸张高度")
                self.entry_calc2_a.focus_set()
                return
            if not b_str:
                messagebox.showerror("错误", "请输入纸张长度")
                self.entry_calc2_b.focus_set()
                return
            if not c_str:
                messagebox.showerror("错误", "请输入张数")
                self.entry_calc2_c.focus_set()
                return
            if not d_str:
                messagebox.showerror("错误", "请输入价格")
                self.entry_calc2_d.focus_set()
                return
                
            # 转换为浮点数
            a = float(a_str)
            b = float(b_str)
            c = float(c_str)
            d = float(d_str)
            
            # 检查除数是否为零
            if a == 0 or b == 0:
                messagebox.showerror("错误", "纸张高度或长度不能为0")
                if a == 0:
                    self.entry_calc2_a.focus_set()
                else:
                    self.entry_calc2_b.focus_set()
                return
            if d == 0:
                messagebox.showerror("错误", "价格不能为0")
                self.entry_calc2_d.focus_set()
                return
                
            # 计算结果
            result = (69 * 138) / (a * b) * (d / c) * 100
            self.calc2_result.set(f"结果：{result:.2f} 元/刀")
            
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字")
            # 聚焦到有问题的输入框
            if not a_str.replace('.', '', 1).isdigit() and a_str:
                self.entry_calc2_a.focus_set()
            elif not b_str.replace('.', '', 1).isdigit() and b_str:
                self.entry_calc2_b.focus_set()
            elif not c_str.replace('.', '', 1).isdigit() and c_str:
                self.entry_calc2_c.focus_set()
            elif not d_str.replace('.', '', 1).isdigit() and d_str:
                self.entry_calc2_d.focus_set()
    
    def show_about(self):
        """显示关于窗口"""
        # 创建新窗口
        about_window = tk.Toplevel(self.root)
        about_window.title("关于")
        about_window.geometry("300x250")
        about_window.resizable(False, False)
        
        # 设置窗口位置（在父窗口中央）
        about_window.transient(self.root)
        about_window.grab_set()
        
        # 窗口内容
        about_label = ttk.Label(
            about_window,
            text="书法纸价格换算器\n\n版本: 1.0\n\n联系方式:\nluwentao@gmail.com",
            font=('Microsoft YaHei', 10),
            justify=tk.CENTER
        )
        about_label.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # 确定按钮
        ok_button = ttk.Button(
            about_window,
            text="确定",
            command=about_window.destroy,
            width=10
        )
        ok_button.pack(pady=(0, 10))
        
        # 设置焦点到确定按钮
        ok_button.focus_set()
        
        # 绑定回车键关闭窗口
        about_window.bind('<Return>', lambda e: about_window.destroy())
    
    def exit_app(self):
        """退出应用程序"""
        if messagebox.askyesno("退出", "确定要退出书法纸价格换算器吗？"):
            self.root.destroy()

def main():
    """主函数"""
    root = tk.Tk()
    app = PaperPriceCalculator(root)
    
    # 设置窗口图标（如果有的话）
    try:
        root.iconbitmap('icon.ico')
    except:
        pass
    
    root.mainloop()

if __name__ == "__main__":
    main()