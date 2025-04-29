# What is System Design?

System design is the process of defining the architecture, components, modules, interfaces, and data flow of a complex software system.

The goal is to create a **scalable**, **reliable**, **maintainable**, and **cost-effective** system.

---

## Key Concepts

- **Scalability:** Ability to handle growth (users, traffic, data).
- **Reliability:** System continues to work even when parts fail.
- **Availability:** System is accessible when needed.
- **Maintainability:** Easy to fix bugs and add new features.
- **Efficiency:** Good performance (low latency, high throughput).

---

## Why System Design?

- Large real-world applications (e.g., Instagram, YouTube, Amazon) can't be built with just simple code.
- We need to think about *scale*, *data flow*, *storage*, *communication* between parts, and *failure handling*.

---

## Example: Design a URL Shortener (like Bitly)

**Problem:**  
Users want to turn a long URL (e.g., `https://example.com/article/1234`) into a short one (e.g., `bit.ly/xyz12`).

**Key questions:**
- How do we create unique short links?
- How do we store and retrieve links efficiently?
- How do we scale when there are millions of users?

✅ Solving these is system design in action.
