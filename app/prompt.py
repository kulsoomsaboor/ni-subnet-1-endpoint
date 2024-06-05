
import os

from decouple import config

from bittensor import Keypair, metagraph, wallet,  logging
import bittensor as bt


import asyncio, traceback


async def query_network(synapse):
         # Configuration and Setup

        # This loads the environment variables from the .env file
        mnemonic = config('MNEMONIC')
        wallet = Keypair.create_from_mnemonic(mnemonic)
        bt.trace()

        metagraph = bt.metagraph(netuid=1, sync=True, lite=False)
        logging.info( f"METAGRAPH SYNCED", )

        den = bt.dendrite(wallet)
        logging.debug(f"dendrite: {den}")

        best_miner = max(range(metagraph.n), key=lambda uid: metagraph.I[uid].item())
        print(best_miner)

        axon_to_query = metagraph.axons[best_miner]
        logging.debug(f"Axons to query: {axon_to_query}")


        response = await den(
            axon_to_query,
            synapse=synapse,
            deserialize=False,
            timeout=500.0,
            streaming=True,
        )


        synapses = []
        synapse=""
        try:
            ii = 0
            async for chunk in response:
                print(f"\nchunk {ii}: {chunk}", end="", flush=True)
                ii += 1
                synapse = chunk  # last object yielded is the synapse itself with completion filled

            synapses.append(synapse)
        except Exception as e:
            print(f"\nError processing response: {traceback.format_exc()}")
        return synapses