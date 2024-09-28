import React from 'react';
interface JsonDataDisplayType {
    jsonData: string|object,
    showkey?:boolean
};

export function JsonDataDisplay({ jsonData, showkey = true }: JsonDataDisplayType) {

        var childshowKey = false;

    if (typeof jsonData === 'object' && !Array.isArray(jsonData))
        return (<>

        

            {jsonData ? (
                    
                   <tr>
                {Object.entries(jsonData).map(([key, value]) =>
                    (
                    (key !== 'status') ? (
                        (typeof value === 'object' && value !== null && !Array.isArray(value))

                            ? (
                                    <JsonDataDisplay jsonData={value} /> 
                           
                            ) : (<td> &nbsp; 
                                <b>{key.toUpperCase()}</b><JsonDataDisplay jsonData={value} />
                                
                        </td>)
                       ) : ('')
                    )
                )

                }
          
          </tr>
            ) : (
                <p>No data available</p>
            )}
        </>

    );
    
        return (<> {Array.isArray(jsonData) ? (
            <>

                
                    {jsonData.map(key =>
                    (
                        
                        (typeof jsonData === 'object' && !Array.isArray(key))
                            ?
                            (<> <JsonDataDisplay jsonData={key} /> </>):('<>Hi</>')
                        
                    )
                    )

                    }
            
            </>
        ) : (
                <td>{jsonData}</td>
        )}
        </>

        );
}

