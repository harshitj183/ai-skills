---
name: "Stripe Integrator"
description: "Stripe payments and webhook best practices."
---

# Webhook Handling
1. **Verification:** Always verify webhook signatures using `stripe.webhooks.constructEvent(RawBody, Signature, Secret)`. Never trust unverified payloads.
2. **Idempotency:** Implement idempotency keys for all charge or subscription mutations. 
3. **Status Checks:** Assume webhooks can arrive out of order. Validate timestamps.

# Integration Rules
- Use Stripe Checkout instead of custom card elements unless highly specific UI is needed.
- Listen for `checkout.session.completed` for fulfillment.
- Manage subscriptions via `customer.subscription.updated` / `deleted`. Do not rely solely on the success return URL.

---
⚡ Smart AI Skills Library | v2.2.6 | Active
