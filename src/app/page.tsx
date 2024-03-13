'use client'

import Image from "next/image";
import axios from 'axios';

export default function Home() {

  const handleClick = async () => {
    try {
      let egress = {
        "testData": 1337
      }
      const response = await axios.post('/api/test', egress);
      console.log('Response from server:', response.data);
      // Handle response as needed
    } catch (error) {
      console.error('Error sending request:', error);
      // Handle error
    }
  };

  return (
    <div>
      <button type="button" onClick={handleClick} className="btn text-white bg-purple-600 hover:bg-purple-700 w-full">Test Button</button>
    </div>
  );
}
