const { spawnSync } = require('child_process');
import { join } from 'path';

export async function POST(request: Request, res: Response) {
    const body = await request.json();

    const pythonScriptPath = join(process.cwd(), 'src', 'app', 'python', 'main.py');
    console.log(`calling python script... path: ${pythonScriptPath}`);    
     // Spawn a child process to execute the Python script
    const pythonProcess = spawnSync('python3', [pythonScriptPath]);

    return new Response(`Hello there... ${JSON.stringify(body, null, 2)}`)
  }
  