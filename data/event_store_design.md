# Foundry AI Event Architecture v1

## Purpose

The Event Architecture is designed to capture every meaningful business action that occurs within Foundry AI.

Instead of storing only the latest state of the application, the system records important business events. This enables historical tracking, debugging, analytics, auditing, AI monitoring, and future data pipeline processing.

The event log represents the history of the platform and acts as a reliable source for understanding how the system reached its current state.

---

# What is an Event?

An event is a record of a meaningful business action that occurred at a specific point in time.

Unlike entities, which represent the current state of the system, events represent facts that have already happened.

Examples:

- Idea Submitted
- Idea Updated
- Idea Deleted
- Validation Started
- Validation Completed
- AI Agent Started
- AI Agent Failed
- AI Agent Completed
- Market Analysis Started
- Market Analysis Completed
- Report Generated
- Report Downloaded

Every event is immutable and should never be modified after it is recorded.

---

# Why Foundry AI Needs Event Logging

Foundry AI is designed as a Data Engineering platform rather than a traditional CRUD application.

Recording business events provides several advantages:

- Preserve historical data
- Support auditing and compliance
- Enable debugging and root cause analysis
- Measure business performance
- Generate analytics dashboards
- Monitor AI agent execution
- Track user behavior
- Support future ETL pipelines
- Enable event replay
- Provide high-quality data for AI model improvement

Without event logging, only the current state of the application is available, making historical analysis impossible.

---

# Business Events to Capture

## User Events

- User Registered
- User Logged In
- User Updated Profile

## Idea Events

- Idea Submitted
- Idea Updated
- Idea Deleted
- Idea Archived

## Validation Events

- Validation Started
- Validation Completed
- Validation Failed

## AI Agent Events

- Agent Started
- Agent Completed
- Agent Failed
- Agent Retried

## Market Analysis Events

- Market Analysis Started
- Market Analysis Completed

## Report Events

- Report Generated
- Report Downloaded
- Report Exported

---

# Events That Should NOT Be Stored

The event store should capture only meaningful business events.

The following interactions should not be stored as business events:

- Mouse movement
- Cursor movement
- Keyboard typing
- Button hover
- Scroll position
- Temporary form edits
- UI animations
- Screen rendering events

These interactions create unnecessary noise and do not contribute to business analytics.

---

# Event Flow in Foundry AI

Business events follow the application architecture before being recorded.

User Request

↓

Router

↓

Validation Engine

↓

Service Layer

↓

Repository Layer

↓

PostgreSQL Database

↓

Business Event Recorded

↓

Event Store

↓

Analytics / Monitoring / Dashboards / Future Data Pipelines

---

# Engineering Principles

1. Store only meaningful business events.

2. Events are immutable.

3. Every event should belong to a business entity.

4. Every event must contain sufficient information to reconstruct business history.

5. Current application state is stored in entity tables.

6. Historical business activity is stored in the event store.

7. Event logging should never replace the primary business transaction but should complement it.

---

# Future Vision

The Event Store will become the foundation for:

- Analytics
- ETL Pipelines
- Business Intelligence
- AI Monitoring
- Dashboarding
- Event Replay
- Kafka Integration
- Streaming Data Processing
- Production Observability

This architecture transforms Foundry AI from a CRUD-based application into a modern event-driven data platform.
