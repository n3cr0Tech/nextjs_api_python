const { spawnSync } = require('child_process');
import { join } from 'path';


const runPythonScript = (successCallback: Function, failCallback:Function, reqBody:any, res:any) => {
  //spawnSync will block the main thread
  //it won't return until the child process has fully closed
  try {
    
    const pythonScriptPath = join(process.cwd(), 'src', 'app', 'python', 'main.py');
    console.log(`calling python script... path: ${pythonScriptPath}`);    
    const resultObj = spawnSync('sudo', ['python3', pythonScriptPath, JSON.stringify(reqBody)]);
    console.log("resultObj: ");
    console.log(resultObj);
    successCallback(resultObj.output.toString(), res);
  } catch(err: any) {
      failCallback(err.message, res);
  }
};

const successReceivedFromPython = (dataFromPython: any, res: any) => {
  console.log(`SUCCESS from python: ${dataFromPython.toString()}`);
  res.status(200).send(dataFromPython);
};

const failReceivedFromPython = (error:any, res: any) => {
  console.log(`ERROR from python: ${error}`);
  res.status(400).json({
    message: 'ERROR - something went wrong UwU',
    error: error
  });
};


export async function POST(request: Request, res: Response) {
    const body = await request.json();
    runPythonScript(successReceivedFromPython, failReceivedFromPython, body, res);
  //  return new Response(`Hello there... ${JSON.stringify(body, null, 2)}`)
}
  