# System Design: URL Shortener (Bitly)

## Problem Statement

Design a service like Bitly that shortens long URLs into short ones.

---

## Requirements

### Functional Requirements:
- Given a long URL, generate a unique short URL.
- Redirect users from the short URL to the original long URL.
- Track how many times a short URL was used (optional).

### Non-Functional Requirements:
- High availability (users expect short links to work 24/7).
- Low latency redirection.
- Scalability (handle millions of links and redirections).

---

## High-Level Architecture

Components:
- Frontend (Website or API to enter URLs)
- Backend Service (generate, store, and retrieve links)
- Database (store mappings between short and long URLs)
- Cache (optional, for fast retrieval)

---

## Database Schema

| Field | Type | Description |
|:------|:-----|:------------|
| id | Primary Key | Unique identifier |
| long_url | Text | Original URL |
| short_code | String | Generated short code |

---

## Short URL Generation Strategies

- Hash the long URL (e.g., using MD5) and use first 6-8 characters.
- Generate a random string and check for collisions.
- Use an incrementing counter and encode it (e.g., Base62).

---

## Potential Bottlenecks and Solutions

| Bottleneck | Solution |
|:-----------|:---------|
| Database lookup too slow | Use caching (e.g., Redis) |
| Collision in short code | Retry on collision |
| Scaling writes | Use database sharding |

---

## Diagram

(See `/diagrams/url-shortener.png`)

---

## Bonus Improvements (Future)

- Custom short links (user can pick custom code)
- Link expiration
- Analytics on link usage
