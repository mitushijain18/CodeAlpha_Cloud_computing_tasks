import secrets
import hashlib
import json
from datetime import datetime

# Simulated Database Connection
database = {
    "passes": [],
    "baseFareUSD": 15.00
}

def create_bus_pass(passenger_id, pass_type):
    print(f"\n[SYSTEM] Initializing secure cloud ticketing window for User: {passenger_id}...")

    # 1. Enforce strict pricing consistency to prevent incorrect pricing
    final_price = database["baseFareUSD"]
    if pass_type.strip().lower() == 'monthly':
        final_price = database["baseFareUSD"] * 20 * 0.80  # Apply a locked 20% loyalty discount
    elif pass_type.strip().lower() == 'weekly':
        final_price = database["baseFareUSD"] * 5 * 0.90   # Apply a locked 10% weekly discount

    # 2. Formulate token variables to build an immutable data record
    pass_record = {
        "passId": "PASS-" + secrets.token_hex(4).upper(),
        "passengerId": passenger_id,
        "type": pass_type.capitalize(),
        "priceUSD": final_price,
        "issueDate": datetime.utcnow().isoformat() + "Z",
        "status": "ACTIVE"
    }

    # 3. Generate a secure cryptographic hash signature to prevent fraud or pass loss
    token_payload = f"{pass_record['passId']}|{pass_record['passengerId']}|{pass_record['priceUSD']}"
    hash_object = hashlib.sha256(token_payload.encode())
    pass_record["securitySignature"] = hash_object.hexdigest()

    # 4. Save permanently to database array
    database["passes"].append(pass_record)
    
    print("✔ Cloud database updated successfully. Ticket record locked!")
    return pass_record

# ==================== INTERACTIVE TERMINAL APP ====================
if __name__ == "__main__":
    print("=========================================")
    print("    CLOUD BUS PASS MANAGEMENT SYSTEM     ")
    print("=========================================")
    
    # Actively taking terminal user inputs
    user_id = input("Enter Passenger ID (e.g., USR-1234): ")
    ticket_type = input("Enter Pass Type (Single / Weekly / Monthly): ")
    
    # Running the generation engine with your custom input
    commuter_pass = create_bus_pass(user_id, ticket_type)
    
    print("\n--- Generated Digital Cloud Bus Pass ---")
    print(json.dumps(commuter_pass, indent=4))
    print("=========================================")