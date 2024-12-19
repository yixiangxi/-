[人工智能与专家系统 第2版 (尹朝庆主编, 主编尹朝庆, 尹朝庆, 尹朝庆主编, 尹朝庆) (Z-Library).pdf](https://www.yuque.com/attachments/yuque/0/2024/pdf/38930558/1734422862548-3af708e8-1289-43eb-9b38-82b640123c79.pdf)

![](https://cdn.nlark.com/yuque/0/2024/png/38930558/1734423112264-e2661385-9e03-4bb7-9ee8-3e7c512e09b5.png)

# 交互界面
字符界面

# 实现语言
使用python语言实现

# 规则库
使用txt文本存储

# 什么是产生式系统
产生式系统（Production System）是一种由一组“产生式”组成的推理系统，广泛应用于人工智能、计算机科学和认知科学领域。它是一种基于规则的推理模型，用来表示和执行智能行为。产生式系统通过不断应用规则来改变世界状态，通常用于模拟专家的决策过程或实现自动推理。



2.产生式系统

把一组产生式放在一起，并让它们互相配合，协同作用，一个产生式生成的结论可以供另一个产生式作为已知事实使用，以求得问题的解决，这样的系统称为产生式系统。一个产生式系统由3个基本部分组成:规则库、综合数据库和控制机构。

(1)规则库。

用于描述相应领域内知识的产生式集合称为规则库。规则库是产生式系统进行问题求解的基础，其中的知识是否完整、一致，表达是否准确，对知识的组织是否合理等，不仅将直接影响到系统的性能，而且还会影响到系统的运行效率,因此对规则库的设计与组织应予以足够

的重视。一般来说，在建立规则库时应注意以下问题:1)有效地表达领域知识。为了使系统具有较强的问题求解能力，除了需要获得足够的知识外，还需要对知识进行有效的表达。为此，需要解决如下一些问题:如何把领域中的知识表达出来，即为了求解领域内的各种问题需要建立哪些产生式规则?知识中的不确定性如何表示?规则库建成后能否对领域内的不同求解问题分别形成相应的推理链,即规则库中的知识是否具有完整性?对于第一个问题,我们可以从下面给出的一个典型例子中得到启发，其他的问题将在后面的章节中予以讨论。

### 产生式系统的基本组成部分：
1. **知识库（或规则库）**：包含一组产生式规则，每条规则通常由“前提”（条件）和“结论”（动作）组成。规则的形式通常为：
    - **IF 条件 THEN 动作** 例如：IF 症状为头痛 AND 发热 THEN 可能是流感。
2. **工作记忆**：表示当前的状态或知识，包含系统当前所知道的信息。在人工智能中，工作记忆通常与当前世界的状态或问题情境有关。
3. **推理机制**：用于选择和应用适当的规则。推理机制会检查工作记忆中的信息是否符合某个规则的条件，如果符合，则触发相应的动作，并更新工作记忆。
4. **控制策略**：决定在何时、如何选择和应用规则，通常涉及选择哪个规则（规则选择机制），以及在应用规则后如何更新工作记忆。

### 产生式系统的工作原理：
1. 系统从初始的工作记忆开始，并检查规则库中的每一条规则。
2. 如果某条规则的条件部分与工作记忆中的信息匹配，则规则被触发，系统执行规则的结论部分。
3. 执行规则的结果是更新工作记忆，这可能影响后续规则的匹配。
4. 系统不断循环执行这些步骤，直到达到终止条件（例如，找到了问题的解决方案或没有更多的规则可应用）。

### 产生式系统的应用：
+ **专家系统**：产生式系统广泛用于构建专家系统，例如医学诊断系统或工程设计系统。
+ **问题求解**：产生式系统可用于解决推理问题，例如棋类游戏的自动玩家。
+ **自动控制**：例如自动驾驶系统或机器人控制。

# 第一步 设计并完成知识库
![](https://cdn.nlark.com/yuque/0/2024/png/38930558/1734423450772-8824fdb8-06c4-41c6-9ed2-7d6ec1cc9044.png)

![](https://cdn.nlark.com/yuque/0/2024/png/38930558/1734423517880-9e80e8e9-5ff2-4c7a-aff7-56386e64c90b.png)

![](https://cdn.nlark.com/yuque/0/2024/png/38930558/1734423549921-f851c2f2-93f6-4b8c-8ff1-cf65b60ca86d.png)

例 2.7 建立一个动物识别系统的规则库，用以识别虎、豹、斑马、长颈鹿、企鹅、鸵鸟、信天翁等7种动物。

解:为了识别这些动物，可以根据动物识别的特征，建立包含下述规则的规则库:

R1:if动物有毛发then 动物是哺乳动物

R2:if动物有奶then动物是哺乳动物

R3:if动物有羽毛then 动物是鸟

R4:if动物会飞and 会生蛋then动物是鸟

R5:if动物吃肉then动物是食肉动物

R6:if动物有锋利牙齿and有爪and眼向前方then动物是食肉动物

R7:if动物是哺乳动物 and 有蹄then 动物是有蹄类动物

R8:if动物是哺乳动物 and 反刍then 动物是有蹄类动物

R9:if动物是哺乳动物 and 是食肉动物 and 有黄褐色皮毛 and 有暗斑点then 动物是豹

R10:if动物是哺乳动物 and 是食肉动物 and 有黄褐色皮毛 and 有黑色条纹 then 动物是虎R11:if动物是有蹄类动物 and 有长脖子 and 有长腿 and 有暗斑点 then 动物是长颈鹿R12:if动物是有蹄类动物 and 有黑色条纹 then 动物是斑马

R13:if动物是鸟 and 不会飞 and 有长脖子 and 有长腿 and 有黑白二色 then 动物是鸵鸟R14:if动物是鸟 and 不会飞 and 会游泳 and 有黑白二色 then动物是企鹅

R15:if动物是鸟 and 善飞then 动物是信天翁



由上述产生式规则可以看出，虽然该系统是用来识别7种动物的，但并不是简单地只设计7条规则分别直接用于识别7种动物。规则设计的基本思想是:首先把动物划分为若干类，如“哺乳动物”、“鸟”、“食肉动物”、“有蹄类动物”等，根据“类”的识别特征建立若千条规则，如规则 R1~R6，然后对属于各类的各个动物根据其个性的识别特征建立各自相应的规则,如规则 R9~R15。这样至少有两个好处，一是当给出的已知事实不完全时，虽然不能推出最终结论，但可能会给出分类结果;二是当需要增加对其他动物(如牛、马等)的识别要求时，规则库中只需增加关于这些动物个性方面的知识，对于规则库中已有的分类知识(如规则 R~

R8)就可以直接使用。2)对知识进行合理的组织与管理。对规则库中的知识进行适当的组织，采用合理的结构形式，可使推理避免访问那些与当前问题求解无关的知识，从而提高问题求解的效率。例如，对例 2.7中的规则库，可根据“哺乳动物”和“鸟”这两类动物的识别规则将 15条规则分为两个子集:

{R1,R2,R5,R6,R7,R8,R9,R10，R11，R12}

(R3,R4，R13，R14，R15}

当待识别动物的识别过程一旦开始使用其中某一个子集的规则时，就可以先只使用该子集中的规则，从而减少查找规则的数量。这种划分还可以逐级进行下去，使得相关的知识构成一个子集或子子集，组成一个层次型的规则库。



(2)**综合数据库**。综合数据库又称为全局数据库，或称为事实库、黑板。综合数据库用于存放问题求解过程中各种当前信息,例如问题的初始事实、原始证据、推理中得到的中间结论(如上例中的“动物是哺乳动物”、“动物是鸟”等)以及最终结论(如上例中的“动物是虎”等)。当规则库中某一条产生式的前提可与综合数据库中的某些已知事实匹配时，该产生式就是一条可用规则，执行可用规则时将该规则的结论放入综合数据库中，作为推理得出的已知事实。可见，综合数据库的内容随着推理的进行是在不断动态变化的。

(3)**控制机构**。

控制机构又称为推理机构或**推理机**，由一组程序组成，可实现对问题的推理求解。**正向推理**的推理机主要功能是:

1)按某种策略从规则库中选择规则与综合数据库中的已知事实进行匹配。匹配是指把规则的前提条件与综合数据库中的已知事实进行比较，如果两者一致，或者近似一致且满足预先规定的近似程度，则称**匹配成功**，相应规则称为可用规则:否则，称为匹配不成功，相应规则不可用于当前的推理。

2)若匹配成功的可用规则有多条，则称为发生冲突。此时，推理机必须执行某种冲突消解策略，从中选出一条可用规则来执行。

3)在执行某一条规则时，如果该规则的后件是一个或多个结论，则把这些结论添加到综合数据库中:如果规则的后件是一个或多个操作，则依序执行这些操作。

4)对于不确定性知识，在执行每一条规则时还要按一定的算法来计算结论的不确定性。

5)随时检查结束推理机运行的条件，在满足结束条件时停止推理机的运行。可见，问题的求解过程是一个不断地从规则库中选取规则与综合数据库中的已知事实进行匹配的过程，每一次成功匹配与执行都使综合数据库增加了新的事实，并向着问题的求解前进了一步，这一过程称为推理。



# 第二步 完成综合数据库及推理机的设计
–描述综合数据库的数据结构

–按书中5.3.2的函数功能，开发正向推理机



5.3.2 正向推理机

产生式系统有正向推理和反向推理两种基本推理方式，本节首先给出用LISP语言编写的正向推理机。

正向推理过程如下:根据在综合数据库中给出的已知事实，正向使用规则，即通过把规则的前件同当前数据库的内容进行匹配来选取可用规则。若有多条规则可用，则按冲突消解策略从中选择一条规则执行，将该规则的结论添加到综合数据库中，直至问题求解或没有可用规则。

LISP语言是函数型语言，因此，用LISP语言实现的正向推理机也是一个函数。首先给出正向推理机需要调用的几个函数的定义，最后给出实现的正向推理机。

用LISP语言编制的产生式系统中的综合数据库的存储结构也是一个表,用facts作为综合数据库表的表名。

**1.函数 recall**

(1)函数表达式:

(recall fact)(2)函数功能:判断变量fact中的一个事实是否在表facts中，若是，recall 返回值是 fact中的事实;否则，返回 nil。

(3)函数定义:

(defun(recall fact)

(cond ((memberfact facts)fact)

```python
def recall(fact, facts):

    # 使用集合的查找操作检查fact是否在facts中
    if fact in facts:
        return fact
    else:
        return None  # 如果未找到，则返回 None，类似于 nil
    """
    判断变量fact中的一个事实是否在facts表中。
    :param fact: 要检查的事实（字符串或其他类型）
    :param facts: 一个包含多个事实的集合或字典
    :return: 如果fact在facts中，返回fact，否则返回nil
    """
# 示例用法：
facts = {'有毛发', '有奶', '会飞', '吃肉'}
fact = '有毛发'

result = recall(fact, facts)
if result:
    print(f"找到事实: {result}")
else:
    print("未找到事实")

```

**2.函数 test-if**

(1)函数表达式:

(test-if rule)

(2)函数功能:判断变量 mule 中的一条规则的前件包含的全部事实是否在表 facts 中，若是，test-if返回t;否则，返回 nil。(3)函数定义:

```python
def test_if(mule, facts):

    # 检查规则前件中的所有事实是否都在facts中
    if all(fact in facts for fact in mule):
        return True  # 如果全部前件条件满足，返回True
    else:
        return None  # 否则返回None
    """
    判断规则的前件是否包含在事实表中。
    :param mule: 包含规则前件的一个集合或列表
    :param facts: 一个包含多个事实的集合
    :return: 如果规则的前件中的所有事实都在facts中，返回True；否则返回None
    """

# 示例用法：
facts = {'有毛发', '有奶', '会飞', '吃肉'}
mule = ['有毛发', '有奶']  # 规则前件

result = test_if(mule, facts)
if result:
    print("规则前件满足，返回t")
else:
    print("规则前件不满足，返回nil")

```



3.**函数remember**

(1)函数表达式:

(remember new)

(2)函数功能:判断变量 new中的一个事实是否在表facts中，若是，remember 返回 nil:否则，将 new中的事实添加到表 facts的表头，且remember 返回 new 中的事实。

(3)函数定义:

```python
def remember(new, facts):

    if new in facts:
        return None  # 如果事实已经存在，则返回None
    else:
        facts.add(new)  # 如果事实不存在，将其添加到facts（假设facts是一个集合）
        return new  # 返回新事实

    """
    判断新事实是否已经存在于事实表中，若已存在返回nil，若不存在则添加到表头并返回新事实。
    :param new: 新的事实（例如字符串）
    :param facts: 一个包含多个事实的集合或列表
    :return: 如果新事实不在facts中，返回新事实并将其添加到facts；否则返回None。
    """
# 示例用法：
facts = {'有毛发', '有奶', '会飞', '吃肉'}  # 假设事实表是一个集合
new_fact = '有蹄'  # 新事实

result = remember(new_fact, facts)
if result:
    print(f"添加新事实: {result}")
else:
    print("新事实已存在，未做添加")
    
# 再次添加相同的事实
new_fact = '有毛发'
result = remember(new_fact, facts)
if result:
    print(f"添加新事实: {result}")
else:
    print("新事实已存在，未做添加")

```



4.函数 use-then

(1)函数表达式:

(use-then rule)

(2)函数功能:判断变量 mule 中的一条规则的后件包含的全部结论是否在表 facts 中，若全部结论都在 facts 中，则 use-then 返回 nil;否则，将不在 facts 中的结论逐一添加到表 facts中，且 use-then 返回t。

```python
def use_then(mule, facts):

    # 找出不在事实表中的结论
    new_conclusions = [conclusion for conclusion in mule if conclusion not in facts]

    if new_conclusions:
        # 如果有结论不在facts中，将这些结论逐一添加到facts中
        for conclusion in new_conclusions:
            facts.add(conclusion)
        return True  # 返回True，表示事实表已更新
    else:
        return None  # 所有结论已在facts中，返回None
    """
    判断规则的后件结论是否都在事实表中。
    :param mule: 包含规则后件结论的一个集合或列表
    :param facts: 包含所有已知事实的集合
    :return: 如果后件结论中的部分未在facts中，返回True并将这些结论添加到facts；否则返回None。
    """

# 示例用法：
facts = {'有毛发', '有奶', '吃肉'}  # 假设事实表是一个集合
mule = ['有毛发', '有奶', '有蹄']  # 规则的后件结论

result = use_then(mule, facts)
if result:
    print(f"更新事实表: {facts}")
else:
    print("所有结论已存在，未做更新")

# 再次调用，检查后件结论是否已更新
mule = ['吃肉', '有黄褐色皮毛']
result = use_then(mule, facts)
if result:
    print(f"更新事实表: {facts}")
else:
    print("所有结论已存在，未做更新")

```

5函数 try-rule

(1)函数表达式:

(try-rule rule)

(2)函数功能:判断规则变量rule中的一条规则的前件包含的全部事实是否在表facts中，若全部事实都在facts中，且规则后件有不在facts 中的结论，则把不在 facts 中的结论逐一添加到表 facts 中，try-rule 返回t;否则，try-rule 返回 nil。(3)函数定义:

```python
def try_rule(rule, facts):

    # 提取规则的前件和后件
    conditions, conclusions = rule
    # 检查规则前件中的所有事实是否都在事实表中
    if all(condition in facts for condition in conditions):
        # 如果前件满足，检查后件中的结论是否有不在facts中的
        new_conclusions = [conclusion for conclusion in conclusions if conclusion not in facts]
        
        if new_conclusions:
            # 将新的结论逐一添加到facts中
            facts.update(new_conclusions)
            return True  # 返回True，表示规则应用成功并更新了事实表
        else:
            return None  # 所有后件结论已在facts中，规则未做更新
    else:
        return None  # 前件不满足，规则不应用

    """
    判断规则的前件是否满足，并根据后件添加新的结论到事实表中。
    :param rule: 一条规则，包括前件和后件（格式为：[前件, 后件]）
    :param facts: 当前所有已知事实的集合
    :return: 如果规则前件满足且有新的结论被添加，返回True；否则返回None。
    """
# 示例用法：
facts = {'有毛发', '有奶', '吃肉'}  # 假设事实表是一个集合

# 规则格式：[前件, 后件]
rule1 = (['有毛发', '有奶'], ['哺乳动物', '有蹄'])  # 规则1
rule2 = (['有毛发', '有奶'], ['哺乳动物'])  # 规则2

# 调用 try_rule 函数
result1 = try_rule(rule1, facts)
result2 = try_rule(rule2, facts)

if result1:
    print(f"规则1应用成功: {facts}")
else:
    print("规则1未应用")

if result2:
    print(f"规则2应用成功: {facts}")
else:
    print("规则2未应用")

```





6.函数step-forward

(1)函数表达式:

(step-forward rules)

(2)函数功能:逐次扫描规则库 rules 中的规则，若发现 rules 中有一条可用规则，即该规则的前件包含的全部事实在表 facts 中，则把该规则的后件中不在 facts 中的所有结论添加到facts 中，且 step-forward 返回 t;若 rles 中没有一条可用规则，则 step-forward 返回 nil。

(3)函数定义:

```python
def step_forward(rules, facts):
 
    for rule in rules:
        conditions, conclusions = rule
        
        # 判断前件是否完全包含在事实表中
        if all(condition in facts for condition in conditions):
            # 找出后件中不在事实表中的结论
            new_conclusions = [conclusion for conclusion in conclusions if conclusion not in facts]
            
            if new_conclusions:
                # 将新的结论逐一添加到事实表
                facts.update(new_conclusions)
                return True  # 返回True，表示规则应用成功并更新了事实表

    return None  # 如果没有规则可以应用，返回None
   """
    扫描规则库，逐条判断规则的前件是否满足，如果满足，则更新事实表。
    :param rules: 规则库，每条规则包含前件和后件的元组
    :param facts: 当前已知的事实集合
    :return: 如果至少有一条规则应用，返回True；否则返回None
    """

# 示例用法：
facts = {'有毛发', '有奶', '吃肉'}  # 假设事实表是一个集合

# 规则库，每条规则是一个元组，包含前件和后件
rules = [
    (['有毛发', '有奶'], ['哺乳动物', '有蹄']),  # 规则1
    (['有毛发', '有奶'], ['哺乳动物']),         # 规则2
    (['有毛发', '有奶', '吃肉'], ['食肉动物'])  # 规则3
]

# 调用 step_forward 函数
result = step_forward(rules, facts)

if result:
    print(f"规则应用成功，更新后的事实表: {facts}")
else:
    print("没有规则可以应用")

```



7.正向推理机函数 deducestep-forward 函数只从rules中选择一条可用规则，并使用该规则对 facts 作一次扩充。推理机要完成推理，通常要对 facts进行多次扩充，也就是说，按扩充了的facts 继续从rules 中选择可用规则，对facts再扩充，直至没有可用规则可选，不能对facts再扩充为止。正向推理机 deduce 可用 step-forward 函数来定义。

(1)函数表达式:

(deducefacts)

(2)函数功能:连续不断地从规则库rules中选择可用规则，每选择到一条可用规则，就把该规则的后件中不在 facts 中的所有结论添加到 facts中，对 facts 扩充，由扩充了的 facts 来选择下一条可用规则对 facts 再次扩充,直至没有可用规则可选为止。若曾找到一条可用规则对 facts进行过一次扩充，则 deduce 返回t;否则，deduce 返回 nil。(3)函数定义:

```python
def deduce(rules, facts):

    # 用来标记是否有任何规则被应用
    updated = False
    
    while True:
        # 使用 step_forward 尝试从规则库中选择一条可用规则并扩充事实
        result = step_forward(rules, facts)
        
        if result:
            updated = True  # 如果规则应用成功，标记更新
        else:
            break  # 如果没有规则可以应用，结束推理过程
    
    return updated  # 如果有任何规则应用过，返回True，否则返回None

    """
    连续不断地从规则库 rules 中选择可用规则，对事实表 facts 进行扩充，
    直到没有更多可用规则为止。如果至少有一次扩充，则返回 True；否则返回 None。
    :param rules: 规则库，每条规则包含前件和后件的元组
    :param facts: 当前所有已知事实的集合
    :return: 如果至少有一次扩充，返回 True；否则返回 None
    """
# step_forward 函数的定义（参考之前的实现）
def step_forward(rules, facts):

    for rule in rules:
        conditions, conclusions = rule
        
        # 判断前件是否完全包含在事实表中
        if all(condition in facts for condition in conditions):
            # 找出后件中不在事实表中的结论
            new_conclusions = [conclusion for conclusion in conclusions if conclusion not in facts]
            
            if new_conclusions:
                # 将新的结论逐一添加到事实表
                facts.update(new_conclusions)
                return True  # 返回True，表示规则应用成功并更新了事实表

    return None  # 如果没有规则可以应用，返回None

    """
    扫描规则库，逐条判断规则的前件是否满足，如果满足，则更新事实表。
    :param rules: 规则库，每条规则包含前件和后件的元组
    :param facts: 当前已知的事实集合
    :return: 如果至少有一条规则应用，返回True；否则返回None
    """
# 示例用法：
facts = {'有毛发', '有奶', '吃肉'}  # 假设事实表是一个集合

# 规则库，每条规则是一个元组，包含前件和后件
rules = [
    (['有毛发', '有奶'], ['哺乳动物', '有蹄']),  # 规则1
    (['有毛发', '有奶'], ['哺乳动物']),         # 规则2
    (['有毛发', '有奶', '吃肉'], ['食肉动物'])  # 规则3
]

# 调用 deduce 函数
result = deduce(rules, facts)

if result:
    print(f"推理完成，更新后的事实表: {facts}")
else:
    print("没有可应用的规则，推理未进行")

```

# 用法
直接运行相应脚本即可
三个ES.py ES2.py ES3.py 三个脚本相互独立，不影响使用，基本功能一致，存在细微差别，ES.py 没有将规则独立出来，ES2.py没有打印具体的推理规则
# 收藏
如果有用的话就标星收藏吧，如果觉得垃圾也欢迎狠狠吐槽