import subprocess
import asyncio
from pyle38.tile38 import Tile38

# Define the new endpoint URL
NEW_ENDPOINT_URL = "https://nuevaurl.actiontracker.eu/api-detections/receive-message"
# Tile38 server
TILE38_SERVER = "redis://localhost:9852"
# Comando para tile38-cli
TILE38_CLI_COMMAND = "tile38-cli -h localhost -p 9852"

# Initialize the Tile38 client
tile38 = Tile38(TILE38_SERVER)

async def update_hooks():
	try:
		#Retrieve all hooks using the HOOKS command
		hooks_response =  await tile38.hooks("*")      
		hooks = hooks_response.hooks

		print(f"Found {len(hooks)} hooks.")

		# Iterate through each hook and update the endpoint URL
		for hook in hooks:
			hook_name = hook.name 
			endpoint_url = hook.endpoints
			meta = hook.meta  
			key = hook.key 
			cmd = hook.command 
			command_str = " ".join(cmd)

			print(f"Processing hook: {hook_name}, Old URL: {endpoint_url}")

			# Replace the endpoint URL with the new one
			new_hook_config = {
				"endpoint": NEW_ENDPOINT_URL,
				"meta": meta,
				"key": key,
				"cmd": cmd,
			}
			
			sethook_command = f"{TILE38_CLI_COMMAND} SETHOOK {hook_name} {NEW_ENDPOINT_URL} {command_str}"
			
			# Execute command SETHOOK ussing subprocess
			process = subprocess.run(sethook_command, shell=True, capture_output=True, text=True)
			if process.returncode != 0:
				print(f"Error executing SETHOOK for hook {hook_name}: {process.stderr}")
			else:
				print(f"Updated hook: {hook_name}, New URL: {NEW_ENDPOINT_URL} , cmd : {command_str}")

	except Exception as e:
		print(f"An error occurred: {e}")
	finally:
		# Close the connection to Tile38
		await tile38.quit()
# Run
if __name__ == "__main__":
	asyncio.run(update_hooks())