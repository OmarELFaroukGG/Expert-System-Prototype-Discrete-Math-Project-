#Star Conflict TPAK Format

The TPAK format is a modified PAK format which Targem uses to store its gamedata in Star Conflict. For compression, it uses the zlib library.

##Sections
1. Header
2. Filename registry
3. File index table
4. File data table 
5. File chunk table
6. Raw chunk data

###Header
Header contains the signature (TPAK), a magic number, a reserved slot and the file count inside the pak.
```C
struct Header {
  char[4] signature; // Should be TPAK
  int magicNumber; // 7
  int unknown1; // 0
  int fileCount; // File count in the pak
  int reserved; // 0
}
```

###Filename Registry
This section contains a header and a compressed table containing the filepaths relative to the directory the pak was archived, layed out in memory in an unusual way. 

####Header

```C
struct FileRegistryHeader {
  int uncompressedSize; // uncompressed size of the filename registry table
  int compressedSize; // compressed size of the table
}
```

####Table 

The next FileRegistryHeader->compressedSize bytes represent the compressed table containing the filepaths. After uncompressing it, XOR the first 4 bytes with the `fileCount` variable from the general header. Table format:

```C
struct FileRegistryEntry
{
  int entrySize; // the number of characters in this filepath/entry (incl. \0)
  char* filepath; // nul terminated string e.g. 'some/file.txt'\0
}
FileRegistryEntry fileRegistry[fileCount]; 
```

###File index table

This section is unclear to what purpose it serves. Its structure is simple:

```C
int fileIndexTable[fileCount]
```

###File data table
This section contains a header and a compressed table similar to the file registry section.

####Header
```C
int compressedSize; //compressed size of the table
```

####Table
The table section looks like `FileDataEntry fileDataTable[fileCount]` - you can calculate its uncompressed size easily. XOR the first 4 bytes of the uncompressed table with `fileCount * header->compressedSize`.

```C
struct FileTableEntry {
  int fileSize; // size of the paked file uncompressed
  int nameOffset; // indicates the offset of this file's path/name in the file registry table as a whole
  int chunkCount; // how many chunks does this file have? usually 1
  int chunkIndex; // index for this file's chunk entry in the file chunk table
};
```

###File chunk table
Stores the file chunk table referenced in the `FileTableEntry` previously. This table does not contain the actual file data, but metadata about the chunks (offset where they're stored, size etc).

Its header looks like this:
```C
struct FileChunkTableHeader {
  int compressedSize; // size of the table compressed
  int chunkCount; // number of entries in the table
}
```

The table is an `FileChunkEntry table[chunkCount]` - its uncompressed size can be calculated. A chunk table entry stores metadata about the file chunk: offset and size. XOR the first 4 bytes of the uncompressed table with the following: `fileCount + header->chunkCount + header->compressedSize`.

```C
struct FileChunkEntry {
	uint32_t fileOffset; // no idea
	uint32_t uncompressedSize; // size of the data chunk uncompressed
	uint32_t dataOffset; // offset position in the chunk data table
	uint32_t compressedSize; // size of the data chunk compressed
}
```
###Raw chunk data
Stores the actual compressed raw data chunks. As mentioned earlier, each file can be split in multiple chunks, but it's usually one chunk. Then the chunks are compressed separately and metadata about them is written in the previous section. 

Using the `FileChunkEntry` metadata, you can index this raw array and extract the chunks separately, then uncompress them and write them to file.

You can find this section's size by seeking to the end of the file.