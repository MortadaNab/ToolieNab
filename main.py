import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.metrics import dp
import math
import re
import os

# تسجيل خط عربي
try:
    LabelBase.register(name='Arabic', fn_regular='fonts/arial.ttf')
except:
    print("Note: Arabic font not found, using default")

# تخصيص شكل التطبيق
Window.clearcolor = (0.12, 0.12, 0.18, 1)  # خلفية داكنة
kivy.config.Config.set('graphics', 'width', '400')
kivy.config.Config.set('graphics', 'height', '700')

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # شعار التطبيق
        logo = Image(source='data/sparta_logo.png' if os.path.exists('data/sparta_logo.png') else 'data/logo.png',
                    size_hint=(1, 0.5))
        
        title = Label(text="أداة سبارتا", font_size=42, font_name='Arabic',
                    color=(0.79, 0.65, 0.97, 1), bold=True)
        
        subtitle = Label(text="رفيقك الدراسي الذكي", font_size=24, font_name='Arabic',
                       color=(0.66, 0.68, 0.78, 1))
        
        layout.add_widget(logo)
        layout.add_widget(title)
        layout.add_widget(subtitle)
        self.add_widget(layout)
        
        # الانتقال للشاشة الرئيسية بعد 2 ثانية
        Clock.schedule_once(self.switch_to_main, 2)
    
    def switch_to_main(self, dt):
        self.manager.current = 'main'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # شعار التطبيق
        logo = Image(source='data/sparta_logo.png' if os.path.exists('data/sparta_logo.png') else 'data/logo.png',
                    size_hint=(1, 0.3))
        
        # عنوان الشاشة
        title = Label(text="أهلاً بك في سبارتا", font_size=32, font_name='Arabic',
                    color=(0.79, 0.65, 0.97, 1), bold=True)
        
        subtitle = Label(text="اختر المادة التي تريد دراستها", font_size=22, font_name='Arabic',
                       color=(0.66, 0.68, 0.78, 1))
        
        layout.add_widget(logo)
        layout.add_widget(title)
        layout.add_widget(subtitle)
        
        # أزرار المواد
        buttons_layout = GridLayout(cols=1, spacing=15, size_hint_y=0.7)
        
        math_btn = Button(text="الرياضيات", font_size=24, font_name='Arabic',
                         background_color=(0.79, 0.65, 0.97, 1),  # بنفسجي
                         background_normal='',
                         on_press=lambda x: self.switch_screen('math'))
        
        physics_btn = Button(text="الفيزياء", font_size=24, font_name='Arabic',
                           background_color=(0.95, 0.54, 0.67, 1),  # وردي
                           background_normal='',
                           on_press=lambda x: self.switch_screen('physics'))
        
        chemistry_btn = Button(text="الكيمياء", font_size=24, font_name='Arabic',
                             background_color=(0.65, 0.89, 0.63, 1),  # أخضر
                             background_normal='',
                             on_press=lambda x: self.switch_screen('chemistry'))
        
        about_btn = Button(text="عن التطبيق", font_size=24, font_name='Arabic',
                         background_color=(0.53, 0.86, 0.92, 1),  # أزرق
                         background_normal='',
                         on_press=lambda x: self.switch_screen('about'))
        
        buttons_layout.add_widget(math_btn)
        buttons_layout.add_widget(physics_btn)
        buttons_layout.add_widget(chemistry_btn)
        buttons_layout.add_widget(about_btn)
        
        layout.add_widget(buttons_layout)
        self.add_widget(layout)
    
    def switch_screen(self, screen_name):
        self.manager.current = screen_name

class MathScreen(Screen):
    def __init__(self, **kwargs):
        super(MathScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # شريط العنوان
        title_bar = BoxLayout(size_hint=(1, 0.1))
        back_btn = Button(text="← رجوع", font_name='Arabic', font_size=18,
                         background_color=(0.4, 0.4, 0.5, 1),
                         background_normal='',
                         on_press=lambda x: self.manager.current='main')
        title = Label(text="أدوات الرياضيات", font_size=28, font_name='Arabic',
                    color=(0.79, 0.65, 0.97, 1), bold=True)
        title_bar.add_widget(back_btn)
        title_bar.add_widget(title)
        
        layout.add_widget(title_bar)
        
        # تبويبات الرياضيات
        tabs = TabbedPanel(do_default_tab=False, tab_pos='top_mid')
        
        # تبويب جدول الضرب
        mult_tab = TabbedPanelItem(text='جدول الضرب', font_name='Arabic')
        mult_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        mult_layout.add_widget(Label(text="أدخل الرقم:", font_name='Arabic', font_size=20, 
                                   color=(0.8, 0.8, 0.9, 1)))
        self.mult_num = TextInput(hint_text="مثال: 5", font_name='Arabic', font_size=24,
                                 size_hint=(1, 0.1), multiline=False)
        mult_layout.add_widget(self.mult_num)
        
        mult_layout.add_widget(Label(text="أدخل الحد الأقصى:", font_name='Arabic', font_size=20,
                                  color=(0.8, 0.8, 0.9, 1)))
        self.mult_limit = TextInput(hint_text="مثال: 10", font_name='Arabic', font_size=24,
                                   size_hint=(1, 0.1), multiline=False)
        mult_layout.add_widget(self.mult_limit)
        
        gen_btn = Button(text="إنشاء الجدول", font_name='Arabic', font_size=24,
                        background_color=(0.79, 0.65, 0.97, 1),
                        background_normal='',
                        on_press=self.generate_table)
        mult_layout.add_widget(gen_btn)
        
        # منطقة عرض الجدول مع تمرير
        scroll_view = ScrollView(size_hint=(1, 0.6))
        self.table_output = Label(text="", font_name='Arabic', font_size=24,
                                color=(0.9, 0.9, 0.9, 1),
                                size_hint_y=None, halign='center')
        self.table_output.bind(texture_size=self.table_output.setter('size'))
        scroll_view.add_widget(self.table_output)
        mult_layout.add_widget(scroll_view)
        
        mult_tab.content = mult_layout
        tabs.add_widget(mult_tab)
        
        # تبويب الآلة الحاسبة
        calc_tab = TabbedPanelItem(text='آلة حاسبة', font_name='Arabic')
        calc_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # شاشة الآلة الحاسبة
        self.calc_display = TextInput(text="0", font_size=32, font_name='Arabic',
                                     readonly=True, halign='right',
                                     background_color=(0.2, 0.2, 0.25, 1),
                                     foreground_color=(1, 1, 1, 1),
                                     size_hint=(1, 0.2))
        calc_layout.add_widget(self.calc_display)
        
        # أزرار الآلة الحاسبة
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+'],
            ['C', '⌫']
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=5)
            for btn in row:
                button = Button(text=btn, font_size=28, font_name='Arabic',
                               background_normal='',
                               on_press=self.on_calc_button_press)
                
                # تخصيص ألوان الأزرار
                if btn in ['C', '⌫']:
                    button.background_color = (0.95, 0.54, 0.67, 1)  # أحمر
                elif btn in ['+', '-', '*', '/']:
                    button.background_color = (0.3, 0.5, 0.7, 1)  # أزرق
                elif btn == '=':
                    button.background_color = (0.65, 0.89, 0.63, 1)  # أخضر
                else:
                    button.background_color = (0.25, 0.25, 0.35, 1)  # رمادي
                
                h_layout.add_widget(button)
            calc_layout.add_widget(h_layout)
        
        calc_tab.content = calc_layout
        tabs.add_widget(calc_tab)
        
        layout.add_widget(tabs)
        self.add_widget(layout)
    
    def generate_table(self, instance):
        try:
            number = int(self.mult_num.text)
            limit = int(self.mult_limit.text)
            
            table = f"جدول ضرب العدد {number}\n\n"
            for i in range(limit + 1):
                result = number * i
                table += f"{number} × {i} = {result}\n"
            
            self.table_output.text = table
            
        except ValueError:
            self.show_error_popup("خطأ", "الرجاء إدخال أرقام صحيحة")
    
    def on_calc_button_press(self, instance):
        current = self.calc_display.text
        
        if instance.text == 'C':
            self.calc_display.text = "0"
        elif instance.text == '⌫':
            self.calc_display.text = current[:-1] if len(current) > 1 else "0"
        elif instance.text == '=':
            try:
                result = eval(current)
                self.calc_display.text = str(result)
            except:
                self.calc_display.text = "خطأ"
        else:
            if current == "0" or current == "خطأ":
                self.calc_display.text = instance.text
            else:
                self.calc_display.text += instance.text
    
    def show_error_popup(self, title, message):
        popup = Popup(title=title, title_font='Arabic',
                     content=Label(text=message, font_name='Arabic'),
                     size_hint=(0.8, 0.4))
        popup.open()

class PhysicsScreen(Screen):
    def __init__(self, **kwargs):
        super(PhysicsScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # شريط العنوان
        title_bar = BoxLayout(size_hint=(1, 0.1))
        back_btn = Button(text="← رجوع", font_name='Arabic', font_size=18,
                         background_color=(0.4, 0.4, 0.5, 1),
                         background_normal='',
                         on_press=lambda x: self.manager.current='main')
        title = Label(text="أدوات الفيزياء", font_size=28, font_name='Arabic',
                    color=(0.95, 0.54, 0.67, 1), bold=True)
        title_bar.add_widget(back_btn)
        title_bar.add_widget(title)
        
        layout.add_widget(title_bar)
        
        # تبويبات الفيزياء
        tabs = TabbedPanel(do_default_tab=False, tab_pos='top_mid')
        
        # تبويب قانون كولوم
        coulomb_tab = TabbedPanelItem(text='قانون كولوم', font_name='Arabic')
        coulomb_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # شرح القانون
        scroll_view = ScrollView()
        formula_box = BoxLayout(orientation='vertical', size_hint_y=None)
        formula_box.bind(minimum_height=formula_box.setter('height'))
        
        formula_box.add_widget(Label(text="قانون كولوم", font_name='Arabic', 
                                   font_size=28, color=(0.95, 0.54, 0.67, 1),
                                   size_hint_y=None, height=dp(60)))
        
        formula_box.add_widget(Label(text="F = k × (q₁ × q₂) / r²", font_size=32,
                                   size_hint_y=None, height=dp(60)))
        
        formula_box.add_widget(Label(text="حيث:", font_name='Arabic', font_size=24,
                                  color=(0.8, 0.8, 0.9, 1),
                                  size_hint_y=None, height=dp(40)))
        
        formula_box.add_widget(Label(text="F: القوة (نيوتن)", font_name='Arabic', font_size=20,
                                  size_hint_y=None, height=dp(30)))
        formula_box.add_widget(Label(text="q₁, q₂: الشحنات (كولوم)", font_name='Arabic', font_size=20,
                                  size_hint_y=None, height=dp(30)))
        formula_box.add_widget(Label(text="r: المسافة (متر)", font_name='Arabic', font_size=20,
                                  size_hint_y=None, height=dp(30)))
        formula_box.add_widget(Label(text="k: ثابت كولوم = 9×10⁹ N·m²/C²", font_size=20,
                                  size_hint_y=None, height=dp(30)))
        
        scroll_view.add_widget(formula_box)
        coulomb_layout.add_widget(scroll_view)
        
        # حقل إدخال الشحنة 1
        coulomb_layout.add_widget(Label(text="الشحنة الأولى (q₁):", font_name='Arabic', font_size=20,
                                     color=(0.8, 0.8, 0.9, 1)))
        
        q1_layout = BoxLayout(spacing=10)
        self.q1_base = TextInput(hint_text="القيمة (مثال: 4)", font_size=24,
                                size_hint=(0.5, None), height=dp(50))
        q1_layout.add_widget(self.q1_base)
        
        q1_layout.add_widget(Label(text="× 10", font_size=24))
        
        self.q1_exp = TextInput(hint_text="الأس (مثال: -6)", font_size=24,
                               size_hint=(0.3, None), height=dp(50))
        q1_layout.add_widget(self.q1_exp)
        
        q1_layout.add_widget(Label(text="C", font_size=24))
        
        coulomb_layout.add_widget(q1_layout)
        
        # حقل إدخال الشحنة 2
        coulomb_layout.add_widget(Label(text="الشحنة الثانية (q₂):", font_name='Arabic', font_size=20,
                                     color=(0.8, 0.8, 0.9, 1)))
        
        q2_layout = BoxLayout(spacing=10)
        self.q2_base = TextInput(hint_text="القيمة (مثال: 3)", font_size=24,
                                size_hint=(0.5, None), height=dp(50))
        q2_layout.add_widget(self.q2_base)
        
        q2_layout.add_widget(Label(text="× 10", font_size=24))
        
        self.q2_exp = TextInput(hint_text="الأس (مثال: -6)", font_size=24,
                               size_hint=(0.3, None), height=dp(50))
        q2_layout.add_widget(self.q2_exp)
        
        q2_layout.add_widget(Label(text="C", font_size=24))
        
        coulomb_layout.add_widget(q2_layout)
        
        # حقل إدخال المسافة
        coulomb_layout.add_widget(Label(text="المسافة (r):", font_name='Arabic', font_size=20,
                                     color=(0.8, 0.8, 0.9, 1)))
        
        r_layout = BoxLayout(spacing=10)
        self.r_val = TextInput(hint_text="مثال: 0.05", font_size=24,
                              size_hint=(0.8, None), height=dp(50))
        r_layout.add_widget(self.r_val)
        r_layout.add_widget(Label(text="m", font_size=24))
        coulomb_layout.add_widget(r_layout)
        
        # زر الحساب
        calc_btn = Button(text="احسب القوة", font_name='Arabic', font_size=24,
                         background_color=(0.95, 0.54, 0.67, 1),
                         background_normal='',
                         on_press=self.calculate_coulomb)
        coulomb_layout.add_widget(calc_btn)
        
        # منطقة النتائج
        coulomb_layout.add_widget(Label(text="النتيجة:", font_name='Arabic', font_size=22,
                                     color=(0.8, 0.8, 0.9, 1)))
        
        self.result_label = Label(text="", font_name='Arabic', font_size=20,
                                color=(0.9, 0.9, 0.9, 1))
        coulomb_layout.add_widget(self.result_label)
        
        coulomb_tab.content = coulomb_layout
        tabs.add_widget(coulomb_tab)
        
        layout.add_widget(tabs)
        self.add_widget(layout)
    
    def calculate_coulomb(self, instance):
        try:
            # Constants
            k = 9e9
            
            # Get values
            q1_base = float(self.q1_base.text)
            q1_exp = float(self.q1_exp.text)
            q2_base = float(self.q2_base.text)
            q2_exp = float(self.q2_exp.text)
            r = float(self.r_val.text)
            
            # Calculate charges
            q1 = q1_base * (10 ** q1_exp)
            q2 = q2_base * (10 ** q2_exp)
            
            # Calculate force
            force = k * (q1 * q2) / (r ** 2)
            
            # Format the result
            result_text = (
                f"خطوات الحساب:\n\n"
                f"1. q₁ = {q1_base} × 10^{q1_exp} = {q1:.2e} C\n"
                f"2. q₂ = {q2_base} × 10^{q2_exp} = {q2:.2e} C\n"
                f"3. r = {r} m\n"
                f"4. r² = {r**2:.4f} m²\n\n"
                f"F = k × (q₁ × q₂) / r²\n"
                f"  = (9 × 10⁹) × ({q1:.2e} × {q2:.2e}) / {r**2:.4f}\n"
                f"  = {force:.4e} N\n\n"
                f"النتيجة: F = {force:.4e} N"
            )
            
            self.result_label.text = result_text
            
        except ValueError:
            self.result_label.text = "خطأ: الرجاء إدخال أرقام صحيحة"

class ChemistryScreen(Screen):
    def __init__(self, **kwargs):
        super(ChemistryScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # شريط العنوان
        title_bar = BoxLayout(size_hint=(1, 0.1))
        back_btn = Button(text="← رجوع", font_name='Arabic', font_size=18,
                         background_color=(0.4, 0.4, 0.5, 1),
                         background_normal='',
                         on_press=lambda x: self.manager.current='main')
        title = Label(text="أدوات الكيمياء", font_size=28, font_name='Arabic',
                    color=(0.65, 0.89, 0.63, 1), bold=True)
        title_bar.add_widget(back_btn)
        title_bar.add_widget(title)
        
        layout.add_widget(title_bar)
        
        # تبويبات الكيمياء
        tabs = TabbedPanel(do_default_tab=False, tab_pos='top_mid')
        
        # تبويب العناصر الكيميائية
        elements_tab = TabbedPanelItem(text='العناصر الكيميائية', font_name='Arabic')
        elements_layout = BoxLayout(orientation='vertical')
        
        # منطقة قابلة للتمرير للعناصر
        scroll_view = ScrollView()
        elements_box = GridLayout(cols=3, spacing=10, padding=10, size_hint_y=None)
        elements_box.bind(minimum_height=elements_box.setter('height'))
        
        # عناصر كيميائية (بالعربية)
        elements = [
            ("الهيدروجين", "H", "1"),
            ("الهيليوم", "He", "2"),
            ("الليثيوم", "Li", "3"),
            ("البريليوم", "Be", "4"),
            ("البورون", "B", "5"),
            ("الكربون", "C", "6"),
            ("النيتروجين", "N", "7"),
            ("الأكسجين", "O", "8"),
            ("الفلور", "F", "9"),
            ("النيون", "Ne", "10"),
            ("الصوديوم", "Na", "11"),
            ("المغنيسيوم", "Mg", "12"),
            ("الألمنيوم", "Al", "13"),
            ("السيليكون", "Si", "14"),
            ("الفوسفور", "P", "15"),
            ("الكبريت", "S", "16"),
            ("الكلور", "Cl", "17"),
            ("الأرجون", "Ar", "18"),
            ("البوتاسيوم", "K", "19"),
            ("الكالسيوم", "Ca", "20"),
            ("التيتانيوم", "Ti", "22"),
            ("الكروم", "Cr", "24"),
            ("المنغنيز", "Mn", "25"),
            ("الحديد", "Fe", "26"),
            ("النيكل", "Ni", "28"),
            ("النحاس", "Cu", "29"),
            ("الزنك", "Zn", "30"),
            ("الزرنيخ", "As", "33"),
            ("البروم", "Br", "35"),
            ("الكريبتون", "Kr", "36"),
            ("السترونشيوم", "Sr", "38"),
            ("الفضة", "Ag", "47"),
            ("القصدير", "Sn", "50"),
            ("اليود", "I", "53"),
            ("الزينون", "Xe", "54"),
            ("الباريوم", "Ba", "56"),
            ("التنجستن", "W", "74"),
            ("البلاتين", "Pt", "78"),
            ("الذهب", "Au", "79"),
            ("الزئبق", "Hg", "80"),
            ("الثاليوم", "Tl", "81"),
            ("الرصاص", "Pb", "82"),
            ("البزموت", "Bi", "83"),
            ("الرادون", "Rn", "86"),
            ("الراديوم", "Ra", "88"),
            ("الأكتينيوم", "Ac", "89"),
            ("الثوريوم", "Th", "90"),
            ("اليورانيوم", "U", "92")
        ]
        
        # إضافة عناوين الأعمدة
        elements_box.add_widget(Label(text="العنصر", font_name='Arabic', font_size=22,
                                    color=(0.65, 0.89, 0.63, 1), 
                                    size_hint_y=None, height=dp(50)))
        elements_box.add_widget(Label(text="الرمز", font_name='Arabic', font_size=22,
                                    color=(0.65, 0.89, 0.63, 1), 
                                    size_hint_y=None, height=dp(50)))
        elements_box.add_widget(Label(text="العدد الذري", font_name='Arabic', font_size=22,
                                    color=(0.65, 0.89, 0.63, 1), 
                                    size_hint_y=None, height=dp(50)))
        
        # إضافة العناصر
        for name, symbol, number in elements:
            elements_box.add_widget(Label(text=name, font_name='Arabic', font_size=18,
                                       size_hint_y=None, height=dp(40)))
            elements_box.add_widget(Label(text=symbol, font_size=18,
                                       size_hint_y=None, height=dp(40)))
            elements_box.add_widget(Label(text=number, font_size=18,
                                       size_hint_y=None, height=dp(40)))
        
        scroll_view.add_widget(elements_box)
        elements_layout.add_widget(scroll_view)
        elements_tab.content = elements_layout
        tabs.add_widget(elements_tab)
        
        layout.add_widget(tabs)
        self.add_widget(layout)

class AboutScreen(Screen):
    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # شريط العنوان
        title_bar = BoxLayout(size_hint=(1, 0.1))
        back_btn = Button(text="← رجوع", font_name='Arabic', font_size=18,
                         background_color=(0.4, 0.4, 0.5, 1),
                         background_normal='',
                         on_press=lambda x: self.manager.current='main')
        title = Label(text="عن التطبيق", font_size=28, font_name='Arabic',
                    color=(0.53, 0.86, 0.92, 1), bold=True)
        title_bar.add_widget(back_btn)
        title_bar.add_widget(title)
        
        layout.add_widget(title_bar)
        
        # منطقة التمرير للمحتوى
        scroll_view = ScrollView()
        content = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))
        
        # محتوى الشاشة
        content.add_widget(Label(text="أداة سبارتا", font_name='Arabic', font_size=32,
                              color=(0.53, 0.86, 0.92, 1), bold=True))
        
        content.add_widget(Label(text="رفيقك الدراسي الذكي", font_name='Arabic', font_size=24,
                              color=(0.7, 0.9, 0.95, 1)))
        
        content.add_widget(Label(text="تطبيق سبارتا هو رفيقك الدراسي الذكي الذي يساعدك في فهم المواد العلمية مثل:", 
                              font_name='Arabic', font_size=20, halign='right'))
        
        content.add_widget(Label(text="• الرياضيات: جدول الضرب وآلة حاسبة متقدمة", 
                              font_name='Arabic', font_size=18))
        content.add_widget(Label(text="• الفيزياء: قانون كولوم وحساب القوة الكهربائية", 
                              font_name='Arabic', font_size=18))
        content.add_widget(Label(text="• الكيمياء: جدول العناصر الكيميائية", 
                              font_name='Arabic', font_size=18))
        
        content.add_widget(Label(text="معلومات التواصل:", font_name='Arabic', font_size=24,
                              color=(0.53, 0.86, 0.92, 1)))
        
        contact_info = [
            "المطور: مرتضى نبيل",
            "البريد الإلكتروني: da0571004@gmail.com",
            "التليجرام: @MortadaNab",
            "GitHub: MortadaNab",
            "Discord: 6uy3"
        ]
        
        for info in contact_info:
            content.add_widget(Label(text=info, font_name='Arabic', font_size=18))
        
        content.add_widget(Label(text="نعمل باستمرار على تحسين التطبيق. نرحب بآرائكم ومقترحاتكم!", 
                              font_name='Arabic', font_size=20, italic=True))
        
        content.add_widget(Label(text="⚡ تعلّم بذكاء، لا بجهد ⚡", 
                              font_name='Arabic', font_size=22, bold=True,
                              color=(0.53, 0.86, 0.92, 1)))
        
        scroll_view.add_widget(content)
        layout.add_widget(scroll_view)
        self.add_widget(layout)

class SpartaApp(App):
    def build(self):
        self.title = "أداة سبارتا"
        self.icon = 'data/sparta_logo.png' if os.path.exists('data/sparta_logo.png') else 'data/icon.png'
        
        # إدارة الشاشات
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(MathScreen(name='math'))
        sm.add_widget(PhysicsScreen(name='physics'))
        sm.add_widget(ChemistryScreen(name='chemistry'))
        sm.add_widget(AboutScreen(name='about'))
        
        return sm

if __name__ == '__main__':
    SpartaApp().run()
