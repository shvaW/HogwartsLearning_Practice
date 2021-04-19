# 测试计算器
import pytest
import yaml
from pytest_hw1.testing.Calculator import Calculator

# 提取数据
def get_datas(keys):
    with open('D:\Workplace\PycharmProjects\Hogwarts_learning\pytest_hw1\datas\datas.yml') as srce:
        datas = yaml.safe_load(srce)
    return datas[keys]['data']

# 测试类
def setup_class():
    print('打开计算器')

def teardown_class():
    print('关闭计算器')

class TestCalc:
    @pytest.mark.parametrize('add_reslt,addnum', get_datas('add'), ids=['single digit', 'double digit',  'false'])
    def test_add(self, add_reslt, addnum):
        print(f'和={add_reslt}, 加数={addnum}')
        assert add_reslt == self.calc.add(*addnum)

    @pytest.mark.parametrize('div_reslt, divnum', get_datas('div'), ids=['int', 'decimal', 'divFalse', 'zeroError'])
    def test_div(self, div_reslt, divnum):
        print(f'商={div_reslt}，[被除数，除数]={divnum}')
        try:
            assert div_reslt == self.calc.div(*divnum)
        except ZeroDivisionError as e:
            print("除数不能为0！！！")
            assert type(e) == ZeroDivisionError
        # else:




    def setup_method(self):
        self.calc = Calculator()
        print('开始测试')

    def teardown_method(self):
        print('测试结束')

if __name__ == '__main__':
    pytest.main()
