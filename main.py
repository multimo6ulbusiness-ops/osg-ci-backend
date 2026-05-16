from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="OSG-CI™ Layer 1 API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Data ──────────────────────────────────────────────────────────────────────

SYSTEM = {
    "name": "OSG-CI™",
    "full_name": "Operational Sovereignty Governance — Competitive Intelligence",
    "layer": "Layer 1B",
    "layer_name": "Constitutional Governance Kernel",
    "system_status": "OPERATIONAL — ALL SERVICES LIVE",
    "tier_achieved": "Tier 2 — Runtime Stabilization",
    "organization": "Olive & Oregano Enterprises",
    "classification": "Internal Engineering Document",
    "build_date": "May 15, 2026",
    "total_containers": 18,
    "total_files": 65,
    "total_directories": 48,
}

HIERARCHY = [
    {"level": "ROOT AUTHORITY", "name": "Human Sovereign", "role": "Priority: 100", "priority": 100},
    {"level": "LAYER 1", "name": "Constitutional Governance Kernel", "role": "Policy Arbiter", "priority": 90},
    {"level": "LAYER 2", "name": "Policy Arbitration Runtime (OPA)", "role": "Rego Rule Engine", "priority": 80},
    {"level": "LAYER 3", "name": "AI Runtime Mesh", "role": "Intelligence Layer", "priority": 70},
    {"level": "LAYER 4", "name": "Operational Services", "role": "Microservice Layer", "priority": 60},
    {"level": "LAYER 5", "name": "Autonomous Intelligence Processes", "role": "RISE Engine", "priority": 50},
]

GOVERNANCE_SERVICES = [
    {"service": "auth-service", "port": 8001, "status": "OPERATIONAL", "function": "JWT issuance/refresh/revoke, RBAC/ABAC, service identity, Keycloak OIDC integration"},
    {"service": "policy-service", "port": 8002, "status": "OPERATIONAL", "function": "OPA governance enforcement, constitutional + operational Rego evaluation, policy logging"},
    {"service": "audit-service", "port": 8003, "status": "OPERATIONAL", "function": "SHA-256 hash-chained immutable event log, ClickHouse analytics, chain integrity verification"},
    {"service": "arbitration-service", "port": 8004, "status": "OPERATIONAL", "function": "Priority-matrix conflict resolution, permission escalation workflow with approve/deny"},
    {"service": "survivability-service", "port": 8005, "status": "OPERATIONAL", "function": "Operational mode FSM (normal→degraded→isolated→recovery→emergency), node quarantine"},
    {"service": "constraint-service", "port": 8006, "status": "OPERATIONAL", "function": "Recursive process registry, propagation depth limits, confidence thresholds, simulation isolation"},
]

INFRASTRUCTURE_SERVICES = [
    {"service": "PostgreSQL 16", "port": 5432, "status": "OPERATIONAL", "function": "Governance/security/audit schemas — users, roles, policies, sessions, constraints, quarantine"},
    {"service": "ClickHouse 23.8", "port": 8123, "status": "OPERATIONAL", "function": "Immutable audit chain analytics, policy evaluation logs, constraint violation history"},
    {"service": "Redis 7", "port": 6379, "status": "OPERATIONAL", "function": "Recursive process registry cache, session tokens, operational state"},
    {"service": "OPA (latest)", "port": 8181, "status": "OPERATIONAL", "function": "Open Policy Agent — evaluates Rego constitutional and operational policies in real-time"},
    {"service": "Keycloak 23", "port": 8180, "status": "OPERATIONAL", "function": "Identity provider — OIDC/OAuth2, MFA, federation, role management"},
    {"service": "Vault 1.15", "port": 8200, "status": "OPERATIONAL", "function": "Secret storage, PKI engine, dynamic credentials, transit encryption"},
    {"service": "Redpanda", "port": 9092, "status": "OPERATIONAL", "function": "Event streaming backbone — Kafka-compatible, sovereign messaging layer"},
    {"service": "MinIO", "port": 9001, "status": "OPERATIONAL", "function": "Long-term audit archive, object storage for immutable event logs"},
]

OBSERVABILITY_SERVICES = [
    {"service": "Grafana", "port": 3000, "status": "OPERATIONAL", "function": "Governance, security, and intelligence dashboards (admin / osg_grafana_secret)"},
    {"service": "Prometheus", "port": 9090, "status": "OPERATIONAL", "function": "Metrics collection across all 6 governance services"},
    {"service": "Loki", "port": 3100, "status": "OPERATIONAL", "function": "Log aggregation — structured logs from all services"},
    {"service": "Jaeger", "port": 16686, "status": "OPERATIONAL", "function": "Distributed tracing — end-to-end request lineage across services"},
]

LIVE_TESTS = [
    {"id": 1, "name": "AI Attempts to Override Human Decision", "result": "DENIED",
     "input": "ai-agent → action: override_human_decision → resource: procurement-order → confidence: 0.99",
     "output": "Constitutional violation: AI systems cannot override human decisions — Human Sovereignty Above AI."},
    {"id": 2, "name": "Human Operator Reads Vendor Catalog", "result": "ALLOWED",
     "input": "commander (human) → action: read → resource: vendor-catalog → confidence: 1.0",
     "output": "No constitutional or operational violations detected. Action permitted."},
    {"id": 3, "name": "Conflict Arbitration: Human vs AI", "result": "HUMAN WINS",
     "input": "commander (root-sovereign, priority 100) vs rise-runtime (ai-operator, priority 70)",
     "output": "commander supersedes rise-runtime. Action: HALT executes. AI propagation blocked."},
    {"id": 4, "name": "Constraint Engine: Low-Confidence Global Propagation", "result": "BLOCKED",
     "input": "rise-ai → action: global_propagation → confidence: 0.55 (below 0.80 threshold)",
     "output": "Confidence 0.55 below minimum 0.80 for action 'global_propagation'. Process terminated."},
    {"id": 5, "name": "Audit Chain: Genesis Block Created", "result": "CHAINED",
     "input": "root-sovereign → event: layer1.boot → service: auth-service",
     "output": "SHA-256 hash: e13b839e4b5d73ac4de983723d6f140e0270070b... Previous: (genesis block). Chain intact."},
    {"id": 6, "name": "Survivability Status", "result": "NORMAL",
     "input": "System mode check → operational_mode",
     "output": "Mode: NORMAL. Transitions: 0. Quarantined nodes: 0. All systems operational."},
]

CONSTITUTIONAL_POLICIES = [
    {"rule": "Autonomous Privilege Escalation", "enforcement": "ALWAYS DENIED", "description": "No AI or service may escalate its own privileges under any condition.", "severity": "critical"},
    {"rule": "Cross-Domain Propagation", "enforcement": "DENIED without auth", "description": "Intelligence cannot cross domain boundaries without explicit human authorization.", "severity": "high"},
    {"rule": "Global Propagation < 80% confidence", "enforcement": "DENIED", "description": "Low-confidence intelligence is constitutionally blocked from system-wide propagation.", "severity": "high"},
    {"rule": "AI Override Human Decision", "enforcement": "ALWAYS DENIED", "description": "AI systems can never override, countermand, or supersede a human decision.", "severity": "critical"},
    {"rule": "Simulation → Production Write", "enforcement": "ALWAYS DENIED", "description": "Simulation environments are constitutionally isolated from production runtimes.", "severity": "critical"},
    {"rule": "Federation Override", "enforcement": "Root-sovereign only", "description": "Only the root-sovereign role may authorize federation-level overrides.", "severity": "high"},
    {"rule": "Governance Bypass", "enforcement": "ALWAYS DENIED", "description": "There is no condition under which governance may be bypassed.", "severity": "critical"},
]

OPERATIONAL_POLICIES = [
    {"condition": "Vendor Risk Score > 0.85", "enforcement": "vendor_approve blocked", "severity": "high"},
    {"condition": "Forecast Confidence < 0.70", "enforcement": "forecast_propagate blocked", "severity": "medium"},
    {"condition": "Data Retention > 7 years", "enforcement": "data_retain blocked", "severity": "medium"},
    {"condition": "audit-observer role", "enforcement": "Read-only — all writes blocked", "severity": "info"},
    {"condition": "Federation sync without key", "enforcement": "federation_sync blocked", "severity": "high"},
    {"condition": "Model validation < 0.75", "enforcement": "model_deploy blocked", "severity": "high"},
]

STABILIZATION_REQUIREMENTS = [
    {"requirement": "Identity Integrity", "status": "COMPLETE", "notes": "auth-service + Keycloak — JWT issuance, RBAC/ABAC, service identity validation"},
    {"requirement": "Policy Enforcement", "status": "COMPLETE", "notes": "policy-service + OPA — constitutional and operational rules active"},
    {"requirement": "Immutable Auditing", "status": "COMPLETE", "notes": "audit-service + ClickHouse — SHA-256 hash-chained event log operational"},
    {"requirement": "Recursive Constraint Enforcement", "status": "COMPLETE", "notes": "constraint-service — propagation limits, confidence thresholds active"},
    {"requirement": "Survivability Controls", "status": "COMPLETE", "notes": "survivability-service — mode FSM, node quarantine, health monitoring"},
    {"requirement": "Permission Arbitration", "status": "COMPLETE", "notes": "arbitration-service — priority matrix, escalation workflow"},
    {"requirement": "Runtime Isolation", "status": "COMPLETE", "notes": "Kubernetes namespace manifests + network policies defined"},
    {"requirement": "Observability Stack", "status": "COMPLETE", "notes": "Prometheus + Grafana + Loki + Jaeger — all operational"},
    {"requirement": "Production Kubernetes Deployment", "status": "PENDING", "notes": "Manifests ready — cluster deployment pending"},
    {"requirement": "Adversarial Stress Testing", "status": "PENDING", "notes": "Layer 3 stabilization — not yet started"},
    {"requirement": "Cryptographic mTLS Validation", "status": "PENDING", "notes": "Certificates defined — runtime validation pending"},
]

STABILIZATION_TIERS = [
    {"tier": "Tier 1", "description": "Conceptual Stabilization — architecture coherent, logic consistent", "status": "COMPLETE"},
    {"tier": "Tier 2", "description": "Runtime Stabilization — services deployed, policies executing, infrastructure live", "status": "COMPLETE"},
    {"tier": "Tier 3", "description": "Adversarial Stabilization — attacks survive, recursive corruption fails", "status": "IN PROGRESS"},
    {"tier": "Tier 4", "description": "Recursive Sovereign Stabilization — intelligence evolves safely under governance", "status": "FUTURE STATE"},
]

TECH_STACK = [
    {"layer": "API Runtime", "technology": "FastAPI + Uvicorn", "version": "0.115 / 0.30", "purpose": "All 6 governance microservices"},
    {"layer": "Identity", "technology": "Keycloak + JWT", "version": "23.0 / HS256", "purpose": "Authentication, RBAC/ABAC, OIDC"},
    {"layer": "Policy Engine", "technology": "Open Policy Agent", "version": "latest", "purpose": "Constitutional + operational rule enforcement"},
    {"layer": "Transactional DB", "technology": "PostgreSQL", "version": "16", "purpose": "Governance, security, audit schemas"},
    {"layer": "Analytics DB", "technology": "ClickHouse", "version": "23.8", "purpose": "Immutable audit chain, policy logs"},
    {"layer": "Cache / Registry", "technology": "Redis", "version": "7", "purpose": "Process registry, session cache"},
    {"layer": "Event Streaming", "technology": "Redpanda", "version": "latest", "purpose": "Kafka-compatible sovereign message bus"},
    {"layer": "Object Storage", "technology": "MinIO", "version": "latest", "purpose": "Long-term audit archive"},
    {"layer": "Secrets", "technology": "HashiCorp Vault", "version": "1.15", "purpose": "PKI, dynamic secrets, encryption"},
    {"layer": "Containers", "technology": "Docker / Compose", "version": "29.4 / v3", "purpose": "Local dev + service orchestration"},
    {"layer": "Orchestration", "technology": "Kubernetes", "version": "manifests", "purpose": "Production namespace isolation"},
    {"layer": "IaC", "technology": "Terraform", "version": "HCL", "purpose": "Reproducible infrastructure provisioning"},
    {"layer": "Metrics", "technology": "Prometheus + Grafana", "version": "latest", "purpose": "System observability"},
    {"layer": "Tracing", "technology": "Jaeger", "version": "latest", "purpose": "Distributed request tracing"},
]

# ── Routes ─────────────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {"status": "OSG-CI™ Layer 1 API operational", "version": "1.0.0"}

@app.get("/api/system")
def get_system():
    return SYSTEM

@app.get("/api/hierarchy")
def get_hierarchy():
    return HIERARCHY

@app.get("/api/services")
def get_services():
    return {
        "governance": GOVERNANCE_SERVICES,
        "infrastructure": INFRASTRUCTURE_SERVICES,
        "observability": OBSERVABILITY_SERVICES,
        "total": len(GOVERNANCE_SERVICES) + len(INFRASTRUCTURE_SERVICES) + len(OBSERVABILITY_SERVICES),
    }

@app.get("/api/tests")
def get_tests():
    return LIVE_TESTS

@app.get("/api/policies")
def get_policies():
    return {
        "constitutional": CONSTITUTIONAL_POLICIES,
        "operational": OPERATIONAL_POLICIES,
    }

@app.get("/api/stabilization")
def get_stabilization():
    return {
        "requirements": STABILIZATION_REQUIREMENTS,
        "tiers": STABILIZATION_TIERS,
    }

@app.get("/api/tech-stack")
def get_tech_stack():
    return TECH_STACK

@app.get("/api/build")
def get_build():
    return {
        "repository": "C:\\Users\\Flerida\\Documents\\osg-ci",
        "total_files": 65,
        "total_directories": 48,
        "docker_compose": "18-container sovereign runtime stack",
        "governance_services": "6 FastAPI microservices (auth, policy, audit, arbitration, survivability, constraint)",
        "policy_engine": "OPA + 2 Rego policy packages (constitutional + operational)",
        "database_schemas": "PostgreSQL — 3 schemas, 20+ tables (governance, security, audit)",
        "audit_engine": "ClickHouse SHA-256 hash-chained immutable event log",
        "kubernetes": "Namespace manifests + network isolation policies for 6 namespaces",
        "terraform": "Infrastructure modules (kubernetes, networking, security, storage) + dev environment",
        "cicd_pipeline": "GitHub Actions — lint → security scan → OPA validation → build+sign → K8s verify → runtime tests",
        "observability": "Prometheus + Grafana + Loki (logs) + Jaeger (tracing)",
        "identity": "Keycloak 23 — 6 sovereign roles with constitutional priority hierarchy",
        "secrets": "HashiCorp Vault 1.15 — dev mode, PKI engine, dynamic credentials",
        "streaming": "Redpanda (Kafka-compatible) + MinIO object storage",
    }

@app.get("/api/compare")
def get_compare():
    return {
        "constitutional_policies": CONSTITUTIONAL_POLICIES,
        "operational_policies": OPERATIONAL_POLICIES,
        "tiers": STABILIZATION_TIERS,
        "summary": {
            "constitutional_count": len(CONSTITUTIONAL_POLICIES),
            "operational_count": len(OPERATIONAL_POLICIES),
            "always_denied": sum(1 for p in CONSTITUTIONAL_POLICIES if p["enforcement"] == "ALWAYS DENIED"),
            "critical_rules": sum(1 for p in CONSTITUTIONAL_POLICIES if p["severity"] == "critical"),
        },
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
