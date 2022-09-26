import copy
from web3 import Web3
from .utils import utils as hero_utils

SERENDALE_CONTRACT_ADDRESS = '0x5F753dcDf9b1AD9AabC1346614D1f4746fd6Ce5C'
CRYSTALVALE_CONTRACT_ADDRESS = '0xEb9B61B145D6489Be575D3603F4a704810e143dF'


ABI = """
[
    {"name": "Approval", "type": "event", "inputs": [{"name": "owner", "type": "address", "internalType": "address", "indexed": true}, {"name": "approved", "type": "address", "internalType": "address", "indexed": true}, {"name": "tokenId", "type": "uint256", "internalType": "uint256", "indexed": true}], "anonymous": false},
    {"name": "ApprovalForAll", "type": "event", "inputs": [{"name": "owner", "type": "address", "internalType": "address", "indexed": true}, {"name": "operator", "type": "address", "internalType": "address", "indexed": true}, {"name": "approved", "type": "bool", "internalType": "bool", "indexed": false}], "anonymous": false},
    {"name": "HeroSummoned", "type": "event", "inputs": [{"name": "owner", "type": "address", "internalType": "address", "indexed": true}, {"name": "heroId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "summonerId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "assistantId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "statGenes", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "RoleAdminChanged", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "previousAdminRole", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "newAdminRole", "type": "bytes32", "internalType": "bytes32", "indexed": true}], "anonymous": false},
    {"name": "RoleGranted", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "account", "type": "address", "internalType": "address", "indexed": true}, {"name": "sender", "type": "address", "internalType": "address", "indexed": true}], "anonymous": false},
    {"name": "RoleRevoked", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "account", "type": "address", "internalType": "address", "indexed": true}, {"name": "sender", "type": "address", "internalType": "address", "indexed": true}], "anonymous": false},
    {"name": "Transfer", "type": "event", "inputs": [{"name": "from", "type": "address", "internalType": "address", "indexed": true}, {"name": "to", "type": "address", "internalType": "address", "indexed": true}, {"name": "tokenId", "type": "uint256", "internalType": "uint256", "indexed": true}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "DEFAULT_ADMIN_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "HERO_MODERATOR_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "MINTER_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "MODERATOR_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "PAUSER_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "approve", "type": "function", "inputs": [{"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "balanceOf", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "burn", "type": "function", "inputs": [{"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "createHero", "type": "function", "inputs": [{"name": "_statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "_visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "_rarity", "type": "uint8", "internalType": "enum IHeroTypes.Rarity"}, {"name": "_shiny", "type": "bool", "internalType": "bool"}, {"name": "_crystal", "type": "tuple", "internalType": "struct ICrystalTypes.HeroCrystal", "components": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "createdBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "summonerTears", "type": "uint8", "internalType": "uint8"}, {"name": "assistantTears", "type": "uint8", "internalType": "uint8"}, {"name": "bonusItem", "type": "address", "internalType": "address"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}]}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "getApproved", "type": "function", "inputs": [{"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "getHero", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "internalType": "struct IHeroTypes.Hero", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "summoningInfo", "type": "tuple", "internalType": "struct IHeroTypes.SummoningInfo", "components": [{"name": "summonedTime", "type": "uint256", "internalType": "uint256"}, {"name": "nextSummonTime", "type": "uint256", "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "summons", "type": "uint32", "internalType": "uint32"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}]}, {"name": "info", "type": "tuple", "internalType": "struct IHeroTypes.HeroInfo", "components": [{"name": "statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "rarity", "type": "uint8", "internalType": "enum IHeroTypes.Rarity"}, {"name": "shiny", "type": "bool", "internalType": "bool"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}, {"name": "class", "type": "uint8", "internalType": "uint8"}, {"name": "subClass", "type": "uint8", "internalType": "uint8"}]}, {"name": "state", "type": "tuple", "internalType": "struct IHeroTypes.HeroState", "components": [{"name": "staminaFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "hpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "mpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint16", "internalType": "uint16"}, {"name": "xp", "type": "uint64", "internalType": "uint64"}, {"name": "currentQuest", "type": "address", "internalType": "address"}, {"name": "sp", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum IHeroTypes.HeroStatus"}]}, {"name": "stats", "type": "tuple", "internalType": "struct IHeroTypes.HeroStats", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hp", "type": "uint16", "internalType": "uint16"}, {"name": "mp", "type": "uint16", "internalType": "uint16"}, {"name": "stamina", "type": "uint16", "internalType": "uint16"}]}, {"name": "primaryStatGrowth", "type": "tuple", "internalType": "struct IHeroTypes.HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "secondaryStatGrowth", "type": "tuple", "internalType": "struct IHeroTypes.HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "professions", "type": "tuple", "internalType": "struct IHeroTypes.HeroProfessions", "components": [{"name": "mining", "type": "uint16", "internalType": "uint16"}, {"name": "gardening", "type": "uint16", "internalType": "uint16"}, {"name": "foraging", "type": "uint16", "internalType": "uint16"}, {"name": "fishing", "type": "uint16", "internalType": "uint16"}]}]}], "stateMutability": "view"},
    {"name": "getRoleAdmin", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "getRoleMember", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "index", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "getRoleMemberCount", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getUserHeroes", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "grantRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "hasRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_name", "type": "string", "internalType": "string"}, {"name": "_symbol", "type": "string", "internalType": "string"}, {"name": "_url", "type": "string", "internalType": "string"}, {"name": "_statScienceAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "name", "type": "string", "internalType": "string"}, {"name": "symbol", "type": "string", "internalType": "string"}, {"name": "baseTokenURI", "type": "string", "internalType": "string"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "isApprovedForAll", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "operator", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "mint", "type": "function", "inputs": [{"name": "to", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "name", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "ownerOf", "type": "function", "inputs": [{"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "renounceRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "revokeRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "safeTransferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "safeTransferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}, {"name": "_data", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setApprovalForAll", "type": "function", "inputs": [{"name": "operator", "type": "address", "internalType": "address"}, {"name": "approved", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setStatScienceAddress", "type": "function", "inputs": [{"name": "_statScienceAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "supportsInterface", "type": "function", "inputs": [{"name": "interfaceId", "type": "bytes4", "internalType": "bytes4"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "symbol", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "tokenByIndex", "type": "function", "inputs": [{"name": "index", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "tokenOfOwnerByIndex", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "index", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "tokenURI", "type": "function", "inputs": [{"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "totalSupply", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "transferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "updateHero", "type": "function", "inputs": [{"name": "_hero", "type": "tuple", "internalType": "struct IHeroTypes.Hero", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "summoningInfo", "type": "tuple", "internalType": "struct IHeroTypes.SummoningInfo", "components": [{"name": "summonedTime", "type": "uint256", "internalType": "uint256"}, {"name": "nextSummonTime", "type": "uint256", "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "summons", "type": "uint32", "internalType": "uint32"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}]}, {"name": "info", "type": "tuple", "internalType": "struct IHeroTypes.HeroInfo", "components": [{"name": "statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "rarity", "type": "uint8", "internalType": "enum IHeroTypes.Rarity"}, {"name": "shiny", "type": "bool", "internalType": "bool"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}, {"name": "class", "type": "uint8", "internalType": "uint8"}, {"name": "subClass", "type": "uint8", "internalType": "uint8"}]}, {"name": "state", "type": "tuple", "internalType": "struct IHeroTypes.HeroState", "components": [{"name": "staminaFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "hpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "mpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint16", "internalType": "uint16"}, {"name": "xp", "type": "uint64", "internalType": "uint64"}, {"name": "currentQuest", "type": "address", "internalType": "address"}, {"name": "sp", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum IHeroTypes.HeroStatus"}]}, {"name": "stats", "type": "tuple", "internalType": "struct IHeroTypes.HeroStats", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hp", "type": "uint16", "internalType": "uint16"}, {"name": "mp", "type": "uint16", "internalType": "uint16"}, {"name": "stamina", "type": "uint16", "internalType": "uint16"}]}, {"name": "primaryStatGrowth", "type": "tuple", "internalType": "struct IHeroTypes.HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "secondaryStatGrowth", "type": "tuple", "internalType": "struct IHeroTypes.HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "professions", "type": "tuple", "internalType": "struct IHeroTypes.HeroProfessions", "components": [{"name": "mining", "type": "uint16", "internalType": "uint16"}, {"name": "gardening", "type": "uint16", "internalType": "uint16"}, {"name": "foraging", "type": "uint16", "internalType": "uint16"}, {"name": "fishing", "type": "uint16", "internalType": "uint16"}]}]}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "userHeroes", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"}
]
    """


def block_explorer_link(contract_address, txid):
    if hasattr(contract_address, 'address'):
        contract_address = str(contract_address.address)
    contract_address = str(contract_address).upper()
    if contract_address == SERENDALE_CONTRACT_ADDRESS.upper():
        return 'https://explorer.harmony.one/tx/' + str(txid)
    elif contract_address == CRYSTALVALE_CONTRACT_ADDRESS.upper():
        return 'https://subnets.avax.network/defi-kingdoms/dfk-chain/explorer/tx/' + str(txid)
    else:
        return str(txid)


def transfer(contract_address, hero_id, private_key, nonce, receiver_address, gas_price_gwei, tx_timeout_seconds, rpc_address, logger=None):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    owner = contract.functions.ownerOf(hero_id).call()
    if logger is not None:
        logger.info("Hero's owner " + str(owner))

    if owner != account.address:
        raise Exception("Owner mismatch")

    tx = contract.functions.transferFrom(owner, receiver_address, hero_id)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.buildTransaction({'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    if logger is not None:
        logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    if logger is not None:
        logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    if logger is not None:
        logger.debug("Transaction successfully sent !")
        logger.info("Waiting for transaction " + block_explorer_link(contract_address, signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds, poll_latency=2)
    if logger is not None:
        logger.info("Transaction mined !")
    logger.info(str(tx_receipt))


def get_owner(contract_address, hero_id, rpc_address, block_identifier="latest"):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return str(contract.functions.ownerOf(hero_id).call(block_identifier=block_identifier))


def get_users_heroes(contract_address, user_address, rpc_address, block_identifier="latest"):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getUserHeroes(Web3.toChecksumAddress(user_address)).call(block_identifier=block_identifier)


def is_approved_for_all(contract_address, owner, operator, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.isApprovedForAll(Web3.toChecksumAddress(owner), Web3.toChecksumAddress(operator)).call()

def set_approval_for_all(contract_address, 
                        operator, 
                        approved, 
                        private_key, 
                        nonce, 
                        gas_price_gwei, 
                        tx_timeout_seconds, 
                        rpc_address, 
                        logger=None):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, 
    abi=ABI)

    tx = contract.functions.setApprovalForAll(operator, approved)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.buildTransaction({'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    if logger is not None:
        logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    if logger is not None:
        logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    if logger is not None:
        logger.debug("Transaction successfully sent !")
        logger.info("Waiting for transaction " + block_explorer_link(contract_address, signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds, poll_latency=2)
    if logger is not None:
        logger.info("Transaction mined !")
        logger.info(str(tx_receipt))    


def get_hero(contract_address, hero_id, rpc_address, block_identifier="latest"):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    contract_entry = contract.functions.getHero(hero_id).call(block_identifier=block_identifier)

    hero = {}
    tuple_index = 0

    hero['id'] = contract_entry[tuple_index]
    tuple_index = tuple_index + 1

    # SummoningInfo
    summoning_info = {}
    summoning_info['summonedTime'] = contract_entry[tuple_index][0]
    summoning_info['nextSummonTime'] = contract_entry[tuple_index][1]
    summoning_info['summonerId'] = contract_entry[tuple_index][2]
    summoning_info['assistantId'] = contract_entry[tuple_index][3]
    summoning_info['summons'] = contract_entry[tuple_index][4]
    summoning_info['maxSummons'] = contract_entry[tuple_index][5]

    hero['summoningInfo'] = summoning_info
    tuple_index = tuple_index + 1

    # HeroInfo
    hero_info = {}
    hero_info['statGenes'] = contract_entry[tuple_index][0]
    hero_info['visualGenes'] = contract_entry[tuple_index][1]
    hero_info['rarity'] = contract_entry[tuple_index][2]
    hero_info['shiny'] = contract_entry[tuple_index][3]
    hero_info['generation'] = contract_entry[tuple_index][4]
    hero_info['firstName'] = contract_entry[tuple_index][5]
    hero_info['lastName'] = contract_entry[tuple_index][6]
    hero_info['shinyStyle'] = contract_entry[tuple_index][7]
    hero_info['class'] = contract_entry[tuple_index][8]
    hero_info['subClass'] = contract_entry[tuple_index][9]

    hero['info'] = hero_info
    tuple_index = tuple_index + 1

    # HeroState
    hero_state = {}
    hero_state['staminaFullAt'] = contract_entry[tuple_index][0]
    hero_state['hpFullAt'] = contract_entry[tuple_index][1]
    hero_state['mpFullAt'] = contract_entry[tuple_index][2]
    hero_state['level'] = contract_entry[tuple_index][3]
    hero_state['xp'] = contract_entry[tuple_index][4]
    hero_state['currentQuest'] = contract_entry[tuple_index][5]
    hero_state['sp'] = contract_entry[tuple_index][6]
    hero_state['status'] = contract_entry[tuple_index][7]

    hero['state'] = hero_state
    tuple_index = tuple_index + 1

    # HeroStats
    hero_stats = {}
    hero_stats['strength'] = contract_entry[tuple_index][0]
    hero_stats['intelligence'] = contract_entry[tuple_index][1]
    hero_stats['wisdom'] = contract_entry[tuple_index][2]
    hero_stats['luck'] = contract_entry[tuple_index][3]
    hero_stats['agility'] = contract_entry[tuple_index][4]
    hero_stats['vitality'] = contract_entry[tuple_index][5]
    hero_stats['endurance'] = contract_entry[tuple_index][6]
    hero_stats['dexterity'] = contract_entry[tuple_index][7]
    hero_stats['hp'] = contract_entry[tuple_index][8]
    hero_stats['mp'] = contract_entry[tuple_index][9]
    hero_stats['stamina'] = contract_entry[tuple_index][10]

    hero['stats'] = hero_stats
    tuple_index = tuple_index + 1

    # primary HeroStatGrowth
    hero_primary_stat_growth = {}
    hero_primary_stat_growth['strength'] = contract_entry[tuple_index][0]
    hero_primary_stat_growth['intelligence'] = contract_entry[tuple_index][1]
    hero_primary_stat_growth['wisdom'] = contract_entry[tuple_index][2]
    hero_primary_stat_growth['luck'] = contract_entry[tuple_index][3]
    hero_primary_stat_growth['agility'] = contract_entry[tuple_index][4]
    hero_primary_stat_growth['vitality'] = contract_entry[tuple_index][5]
    hero_primary_stat_growth['endurance'] = contract_entry[tuple_index][6]
    hero_primary_stat_growth['dexterity'] = contract_entry[tuple_index][7]
    hero_primary_stat_growth['hpSm'] = contract_entry[tuple_index][8]
    hero_primary_stat_growth['hpRg'] = contract_entry[tuple_index][9]
    hero_primary_stat_growth['hpLg'] = contract_entry[tuple_index][10]
    hero_primary_stat_growth['mpSm'] = contract_entry[tuple_index][11]
    hero_primary_stat_growth['mpRg'] = contract_entry[tuple_index][12]
    hero_primary_stat_growth['mpLg'] = contract_entry[tuple_index][13]

    hero['primaryStatGrowth'] = hero_primary_stat_growth
    tuple_index = tuple_index + 1

    # secondary HeroStatGrowth
    hero_secondary_stat_growth = {}
    hero_secondary_stat_growth['strength'] = contract_entry[tuple_index][0]
    hero_secondary_stat_growth['intelligence'] = contract_entry[tuple_index][1]
    hero_secondary_stat_growth['wisdom'] = contract_entry[tuple_index][2]
    hero_secondary_stat_growth['luck'] = contract_entry[tuple_index][3]
    hero_secondary_stat_growth['agility'] = contract_entry[tuple_index][4]
    hero_secondary_stat_growth['vitality'] = contract_entry[tuple_index][5]
    hero_secondary_stat_growth['endurance'] = contract_entry[tuple_index][6]
    hero_secondary_stat_growth['dexterity'] = contract_entry[tuple_index][7]
    hero_secondary_stat_growth['hpSm'] = contract_entry[tuple_index][8]
    hero_secondary_stat_growth['hpRg'] = contract_entry[tuple_index][9]
    hero_secondary_stat_growth['hpLg'] = contract_entry[tuple_index][10]
    hero_secondary_stat_growth['mpSm'] = contract_entry[tuple_index][11]
    hero_secondary_stat_growth['mpRg'] = contract_entry[tuple_index][12]
    hero_secondary_stat_growth['mpLg'] = contract_entry[tuple_index][13]

    hero['secondaryStatGrowth'] = hero_secondary_stat_growth
    tuple_index = tuple_index + 1

    # HeroProfessions
    hero_professions = {}
    hero_professions['mining'] = contract_entry[tuple_index][0]
    hero_professions['gardening'] = contract_entry[tuple_index][1]
    hero_professions['foraging'] = contract_entry[tuple_index][2]
    hero_professions['fishing'] = contract_entry[tuple_index][3]

    hero['professions'] = hero_professions

    return hero


def human_readable_hero(raw_hero, hero_male_first_names=None, hero_female_first_names=None, hero_last_names=None):
    readable_hero = copy.deepcopy(raw_hero)

    readable_hero['info']['rarity'] = hero_utils.parse_rarity(readable_hero['info']['rarity'])
    readable_hero['info']['class'] = hero_utils.parse_class(readable_hero['info']['class'])
    readable_hero['info']['subClass'] = hero_utils.parse_class(readable_hero['info']['subClass'])

    # visualGenes
    readable_hero['info']['visualGenes'] = hero_utils.parse_visual_genes(readable_hero['info']['visualGenes'])

    # statsGenes
    readable_hero['info']['statGenes'] = hero_utils.parse_stat_genes(readable_hero['info']['statGenes'])

    # names
    if readable_hero['info']['visualGenes']['gender'] == 'male':
        if hero_male_first_names is not None:
            readable_hero['info']['firstName'] = hero_male_first_names[readable_hero['info']['firstName']]
    else:
        if hero_female_first_names is not None:
            readable_hero['info']['firstName'] = hero_female_first_names[readable_hero['info']['firstName']]

    if hero_last_names is not None:
        readable_hero['info']['lastName'] = hero_last_names[readable_hero['info']['lastName']]

    return readable_hero
