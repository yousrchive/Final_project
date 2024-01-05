package com.example.basic.model.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
public class WebDto {
    private long uid;
    private String id;
    private String password;
    private String name;
    private int age;
    private String role;
}
