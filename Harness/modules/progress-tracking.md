# Module: Progress Tracking

↩️ [返回概览](../SKILL.md)

## progress.txt 用途

**仅记录高层级决策和进度** - 关键里程碑、重大问题、需要关注的点。

不是详细任务列表（那是 feature_list.json 的职责）。

## 格式

```
[2026-03-16 10:30] Started working on Calculator feature
[2026-03-16 11:45] Decision: Use TDD approach for this module
[2026-03-17 09:00] Completed Calculator - all tests passing
[2026-03-17 14:20] Blocked: Token refresh logic has bug, need to fix
```

## 规则

1. **简洁** - 一句话说明状态
2. **含时间戳** - `[YYYY-MM-DD HH:MM]` 格式
3. **含决策** - 重要的技术决策要记录
4. **含问题** - 遇到的重大问题要记录
5. **关联 feature** - 提及对应的 feature 名称

## 示例

| 场景 | 记录内容 |
|------|----------|
| 开始功能 | `[YYYY-MM-DD HH:MM] Started working on [Feature]` |
| 完成功能 | `[YYYY-MM-DD HH:MM] Completed [Feature] - all tests passing` |
| 遇到问题 | `[YYYY-MM-DD HH:MM] Blocked: [Feature] - [issue description]` |
| 技术决策 | `[YYYY-MM-DD HH:MM] Decision: [what was decided]` |
| 交接记录 | `[YYYY-MM-DD HH:MM] Handover: [what's done, what's pending]` |
