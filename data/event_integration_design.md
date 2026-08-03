# Event Integration Design

## Objective

This document defines where business events should be recorded within the Foundry AI architecture.

The goal is to integrate event logging without violating software engineering principles such as Separation of Concerns, Single Responsibility Principle (SRP), and Repository Pattern.

---

# Option 1 - Router Layer

## Advantages

- Has access to every incoming request.
- Easy to trigger event logging.

## Disadvantages

- Router should only handle HTTP requests and responses.
- Business logic should not exist here.
- Makes routers difficult to maintain.

Verdict:
 Not Recommended

---

# Option 2 - Validation Layer

## Advantages

- Validation executes before business logic.

## Disadvantages

- Validation is responsible only for checking data correctness.
- Successful validation does not mean a business event occurred.
- Violates Single Responsibility Principle.

Verdict:
 Not Recommended

---

# Option 3 - Service Layer

## Advantages

- Contains business logic.
- Knows whether an operation succeeded or failed.
- Can coordinate multiple repositories.
- Best location to generate business events.
- Easy to extend and maintain.

## Disadvantages

- Slightly increases service complexity.
- Requires an additional Event Service.

Verdict:
 Recommended

---

# Option 4 - Repository Layer

## Advantages

- Has direct access to the database.

## Disadvantages

- Repository should only perform database operations.
- Business events are business logic, not persistence logic.
- Violates Repository Pattern.

Verdict:
 Not Recommended

---

# Option 5 - Database Trigger

## Advantages

- Automatic event generation.
- Independent of application code.

## Disadvantages

- Difficult to debug.
- Business logic becomes hidden inside the database.
- Harder to version control.
- Not portable across database systems.

Verdict:
 Not Recommended

---

# Final Decision

## Selected Layer

Service Layer

## Reason

The Service Layer represents the business workflow of the application.

It knows when a business operation begins, succeeds, fails, or requires retry.

After completing a successful business operation, the Service Layer will invoke the Event Service to record the corresponding business event.

This keeps responsibilities separated while maintaining a clean and scalable architecture.

Future workflow:

Request

↓

Router

↓

Validation

↓

Service

├── Business Operation

└── Event Service

↓

Repository

↓

PostgreSQL

↓

Response

This architecture follows modern software engineering principles and prepares Foundry AI for future event-driven processing, analytics, monitoring, and streaming integrations.
