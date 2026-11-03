import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Nomad',
  description: '我的讲义站点',
  srcDir: '.',
  base: '/nomad/',
  cleanUrls: true,
  ignoreDeadLinks: true,
  themeConfig: {
    nav: [
      { text: '首页', link: '/' }
    ],
    sidebar: [
      {
        text: '讲义',
        items: [
          { text: "AGENTS", link: "/AGENTS" },
          { text: "Coursera/[0]示例/(1)示例课程/(0)示例笔记", link: "/Coursera/[0]示例/(1)示例课程/(0)示例笔记" },
          { text: "Coursera/[1]数学/(1)数学分析/(1)数列的极限", link: "/Coursera/[1]数学/(1)数学分析/(1)数列的极限" },
          { text: "Coursera/[1]数学/(1)数学分析/(10)平面曲线", link: "/Coursera/[1]数学/(1)数学分析/(10)平面曲线" },
          { text: "Coursera/[1]数学/(1)数学分析/(11)定性作图", link: "/Coursera/[1]数学/(1)数学分析/(11)定性作图" },
          { text: "Coursera/[1]数学/(1)数学分析/(12)全局行为分析", link: "/Coursera/[1]数学/(1)数学分析/(12)全局行为分析" },
          { text: "Coursera/[1]数学/(1)数学分析/(2)数列的分析性质", link: "/Coursera/[1]数学/(1)数学分析/(2)数列的分析性质" },
          { text: "Coursera/[1]数学/(1)数学分析/(3)函数的极限", link: "/Coursera/[1]数学/(1)数学分析/(3)函数的极限" },
          { text: "Coursera/[1]数学/(1)数学分析/(4)函数的连续性", link: "/Coursera/[1]数学/(1)数学分析/(4)函数的连续性" },
          { text: "Coursera/[1]数学/(1)数学分析/(5)函数极限的意义", link: "/Coursera/[1]数学/(1)数学分析/(5)函数极限的意义" },
          { text: "Coursera/[1]数学/(1)数学分析/(6)函数的导数", link: "/Coursera/[1]数学/(1)数学分析/(6)函数的导数" },
          { text: "Coursera/[1]数学/(1)数学分析/(7)连续函数", link: "/Coursera/[1]数学/(1)数学分析/(7)连续函数" },
          { text: "Coursera/[1]数学/(1)数学分析/(8)函数的展开", link: "/Coursera/[1]数学/(1)数学分析/(8)函数的展开" },
          { text: "Coursera/[1]数学/(1)数学分析/(9)复杂函数的极限", link: "/Coursera/[1]数学/(1)数学分析/(9)复杂函数的极限" },
          { text: "Coursera/[1]数学/(2)线性代数/(1)线性方程组", link: "/Coursera/[1]数学/(2)线性代数/(1)线性方程组" },
          { text: "Coursera/[1]数学/(2)线性代数/(2)矩阵", link: "/Coursera/[1]数学/(2)线性代数/(2)矩阵" },
          { text: "Coursera/[1]数学/(2)线性代数/(3)向量空间", link: "/Coursera/[1]数学/(2)线性代数/(3)向量空间" },
          { text: "Coursera/[1]数学/(2)线性代数/(4)线性映射与线性变换", link: "/Coursera/[1]数学/(2)线性代数/(4)线性映射与线性变换" },
          { text: "Coursera/[1]数学/(2)线性代数/(5)内积空间", link: "/Coursera/[1]数学/(2)线性代数/(5)内积空间" },
          { text: "Coursera/[1]数学/(2)线性代数/(6)特征值与特征向量", link: "/Coursera/[1]数学/(2)线性代数/(6)特征值与特征向量" },
          { text: "Coursera/[1]数学/(2)线性代数/(7)二次型", link: "/Coursera/[1]数学/(2)线性代数/(7)二次型" },
          { text: "Coursera/[1]数学/(2)线性代数/(8)复数矩阵与复线性代数", link: "/Coursera/[1]数学/(2)线性代数/(8)复数矩阵与复线性代数" },
          { text: "Coursera/[1]数学/(2)线性代数/(9)向量范数与矩阵范数", link: "/Coursera/[1]数学/(2)线性代数/(9)向量范数与矩阵范数" },
          { text: "Coursera/[2]电子/(1)RoboMaster电控/(1)robomaster电控", link: "/Coursera/[2]电子/(1)RoboMaster电控/(1)robomaster电控" },
          { text: "Coursera/[2]电子/(2)Python程序设计/(1)函数对象与基本输入输出", link: "/Coursera/[2]电子/(2)Python程序设计/(1)函数对象与基本输入输出" },
          { text: "Coursera/[2]电子/(2)Python程序设计/(2)数值类型及其运算", link: "/Coursera/[2]电子/(2)Python程序设计/(2)数值类型及其运算" },
          { text: "Coursera/[2]电子/(2)Python程序设计/(3)选择结构", link: "/Coursera/[2]电子/(2)Python程序设计/(3)选择结构" },
          { text: "Coursera/[2]电子/(2)Python程序设计/(4)字符串", link: "/Coursera/[2]电子/(2)Python程序设计/(4)字符串" },
          { text: "Coursera/[2]电子/(2)Python程序设计/(5)循环结构", link: "/Coursera/[2]电子/(2)Python程序设计/(5)循环结构" },
          { text: "Coursera/[2]电子/(2)Python程序设计/(6)列表", link: "/Coursera/[2]电子/(2)Python程序设计/(6)列表" },
          { text: "Coursera/[2]电子/(2)Python程序设计/(7)列表进阶与元组", link: "/Coursera/[2]电子/(2)Python程序设计/(7)列表进阶与元组" },
          { text: "Coursera/[2]电子/(3)C语言程序设计/(1)第1章 程序设计基础", link: "/Coursera/[2]电子/(3)C语言程序设计/(1)第1章%20程序设计基础" },
          { text: "Coursera/[2]电子/(3)C语言程序设计/(2)第2章 数据与表达式", link: "/Coursera/[2]电子/(3)C语言程序设计/(2)第2章%20数据与表达式" },
          { text: "Coursera/[2]电子/(3)C语言程序设计/(3)第3章 结构化程序设计", link: "/Coursera/[2]电子/(3)C语言程序设计/(3)第3章%20结构化程序设计" },
          { text: "Coursera/[2]电子/(3)C语言程序设计/(4)第4章 数组", link: "/Coursera/[2]电子/(3)C语言程序设计/(4)第4章%20数组" },
          { text: "Coursera/[2]电子/(3)C语言程序设计/(5)第5章 函数", link: "/Coursera/[2]电子/(3)C语言程序设计/(5)第5章%20函数" },
          { text: "Coursera/[2]电子/(3)C语言程序设计/(6)第6章 指针和引用", link: "/Coursera/[2]电子/(3)C语言程序设计/(6)第6章%20指针和引用" },
          { text: "Coursera/[2]电子/(3)C语言程序设计/(7)第7章 结构类型与链表", link: "/Coursera/[2]电子/(3)C语言程序设计/(7)第7章%20结构类型与链表" },
          { text: "Coursera/[2]电子/(3)C语言程序设计/(8)第8章 文件", link: "/Coursera/[2]电子/(3)C语言程序设计/(8)第8章%20文件" },
          { text: "Coursera/[2]电子/(3)C语言程序设计/(9)第9章 算法", link: "/Coursera/[2]电子/(3)C语言程序设计/(9)第9章%20算法" },
          { text: "README", link: "/README" },
          { text: "STYLES", link: "/STYLES" }
        ]
      }
    ],
    search: {
      provider: 'local'
    }
  }
})
