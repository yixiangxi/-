def read_rules_from_file(filename="regular.txt"):
    rules = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():  # 忽略空行
                    try:
                        # 使用eval()读取并转换为Python元组形式
                        rule = eval(line.strip())
                        # 检查规则是否符合预期的格式：元组，包含两个元素（条件列表，结论列表）
                        if isinstance(rule, tuple) and len(rule) == 2:
                            conditions, conclusions = rule
                            # 确保条件和结论都是列表
                            if isinstance(conditions, list) and isinstance(conclusions, list):
                                rules.append(rule)
                            else:
                                print(f"格式错误：条件或结论部分不是列表：{rule}")
                        else:
                            print(f"格式错误：规则不是包含两个元素的元组：{rule}")
                    except Exception as e:
                        print(f"规则解析失败：{line.strip()}，错误：{e}")
    except FileNotFoundError:
        print(f"错误：文件 {filename} 未找到。")
    return rules


# 定义推理机所需的辅助函数：recall, test-if, remember, use-then, try-rule, step-forward, deduce
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


# 主函数：从文件中读取规则，获取用户输入的事实，并进行推理
def main():
    # 从文件中读取规则
    rules = read_rules_from_file("regular.txt")

    if not rules:
        print("没有规则可供推理，程序结束。")
        return
    count = 0
    while count < 5:    # 获取用户输入的事实
        facts = set(input("请输入已知的动物事实（用逗号分隔）：").strip().split("，"))
        facts = {fact.strip() for fact in facts}  # 去除每个事实前后的空格

        print(f"初始事实表：{facts}")

        # 使用deduce进行推理
        result = deduce(rules, facts)

        if result:
            print(f"推理完成，更新后的事实表: {facts}")
        else:
            print("没有可应用的规则，推理未进行")
        count += 1


if __name__ == "__main__":
    main()
