# 假设我们已经定义好了推理系统的各个辅助函数：recall, test-if, remember, use-then, try-rule, step-forward, deduce

def recall(fact, facts):
    """返回事实fact是否在facts中"""
    return fact if fact in facts else None

def test_if(rule, facts):
    """检查规则rule的前件是否在facts中"""
    conditions, _ = rule
    return all(condition in facts for condition in conditions)

def remember(new_fact, facts):
    """如果new_fact不在facts中，添加并返回new_fact，否则返回None"""
    if new_fact not in facts:
        facts.add(new_fact)
        return new_fact
    return None

def use_then(rule, facts):
    """应用规则后件，判断后件是否都已经在facts中"""
    _, conclusions = rule
    new_conclusions = [conclusion for conclusion in conclusions if conclusion not in facts]
    if new_conclusions:
        facts.update(new_conclusions)
        return True
    return False

def try_rule(rule, facts):
    """如果规则的前件满足，且后件有新的结论，将新的结论添加到facts"""
    conditions, conclusions = rule
    if test_if(rule, facts):
        new_conclusions = [conclusion for conclusion in conclusions if conclusion not in facts]
        if new_conclusions:
            facts.update(new_conclusions)
            return True
    return False

def step_forward(rules, facts):
    """从规则库中选择一条可用规则应用于事实表"""
    for rule in rules:
        if try_rule(rule, facts):
            return True
    return None

def deduce(rules, facts):
    """连续调用step-forward进行推理，直到没有更多规则可以应用"""
    updated = False
    while True:
        result = step_forward(rules, facts)
        if result:
            updated = True
        else:
            break
    return updated

# 规则库：每条规则由前件（条件）和后件（结论）组成
rules = [
    (['有毛发'], ['哺乳动物']),  # 规则1：有毛发 -> 哺乳动物
    (['有奶'], ['哺乳动物']),  # 规则2：有奶 -> 哺乳动物
    (['有羽毛'], ['鸟']),  # 规则3：有羽毛 -> 鸟
    (['会飞', '会生蛋'], ['鸟']),  # 规则4：会飞并且会生蛋 -> 鸟
    (['吃肉'], ['食肉动物']),  # 规则5：吃肉 -> 食肉动物
    (['有锋利牙齿', '有爪', '眼向前方'], ['食肉动物']),  # 规则6：有锋利牙齿、有爪、眼向前方 -> 食肉动物
    (['有蹄'], ['有蹄类动物']),  # 规则7：有蹄 -> 有蹄类动物
    (['反刍'], ['有蹄类动物']),  # 规则8：反刍 -> 有蹄类动物
    (['哺乳动物', '有黄褐色皮毛', '有暗斑点'], ['豹']),  # 规则9：哺乳动物、有黄褐色皮毛、有暗斑点 -> 豹
    (['哺乳动物', '有黄褐色皮毛', '有黑色条纹'], ['虎']),  # 规则10：哺乳动物、有黄褐色皮毛、有黑色条纹 -> 虎
    (['有长脖子', '有长腿', '有暗斑点'], ['长颈鹿']),  # 规则11：有长脖子、有长腿、有暗斑点 -> 长颈鹿
    (['有黑色条纹'], ['斑马']),  # 规则12：有黑色条纹 -> 斑马
    (['不会飞', '有长脖子', '有长腿', '黑白二色'], ['鸵鸟']),  # 规则13：不会飞、有长脖子、有长腿、黑白二色 -> 鸵鸟
    (['不会飞', '会游泳', '黑白二色'], ['企鹅']),  # 规则14：不会飞、会游泳、黑白二色 -> 企鹅
    (['善飞'], ['信天翁'])  # 规则15：善飞 -> 信天翁
]

# 示例事实：假设我们已知一些动物的特征
facts = {'有毛发', '吃肉'}  # 假设初始已知事实是：动物有毛发，吃肉

# 使用deduce函数进行推理，得到结果
result = deduce(rules, facts)

if result:
    print(f"推理完成，更新后的事实表: {facts}")
else:
    print("没有可应用的规则，推理未进行")
